import 'jsr:@supabase/functions-js/edge-runtime.d.ts'
import { createClient } from 'npm:@supabase/supabase-js@2'

type Keyword = 'COACH' | 'PROGRAM' | 'LOCATION' | 'SEASON'
type Channel = 'instagram' | 'facebook'
type ContentType = 'post' | 'reel' | 'unknown'
type Status =
  | 'received'
  | 'ignored_no_keyword'
  | 'ignored_duplicate'
  | 'ignored_spam'
  | 'eligible'
  | 'dm_sent'
  | 'dm_failed'

type CommentEventInsert = {
  channel: Channel
  content_type: ContentType
  post_id: string
  comment_id: string
  commenter_platform_user_id: string
  commenter_username: string | null
  comment_text: string
  comment_text_normalized: string | null
  matched_keywords: string[]
  keyword_detected: Keyword | null
  is_spam: boolean
  should_send_dm: boolean
  dm_sent: boolean
  dm_sent_at: string | null
  status: Status
  raw_webhook_payload: Record<string, unknown>
}

const SUPABASE_URL = Deno.env.get('SUPABASE_URL')
const SUPABASE_SERVICE_ROLE_KEY = Deno.env.get('SUPABASE_SERVICE_ROLE_KEY')
const META_WEBHOOK_VERIFY_TOKEN = Deno.env.get('META_WEBHOOK_VERIFY_TOKEN')

if (!SUPABASE_URL || !SUPABASE_SERVICE_ROLE_KEY || !META_WEBHOOK_VERIFY_TOKEN) {
  throw new Error(
    'Missing required env vars: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY, META_WEBHOOK_VERIFY_TOKEN',
  )
}

const supabase = createClient(SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY)

function json(data: unknown, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  })
}

function normalizeText(input: string | null | undefined): string | null {
  if (!input) return null

  return input
    .normalize('NFKD')
    .replace(/[^\p{L}\p{N}\s]/gu, ' ')
    .replace(/\s+/g, ' ')
    .trim()
    .toUpperCase()
}

function detectKeywords(normalized: string | null): Keyword[] {
  if (!normalized) return []

  const words = new Set(normalized.split(/\s+/).filter(Boolean))
  const matches: Keyword[] = []

  if (words.has('COACH')) matches.push('COACH')
  if (words.has('PROGRAM')) matches.push('PROGRAM')
  if (words.has('LOCATION')) matches.push('LOCATION')
  if (words.has('SEASON')) matches.push('SEASON')

  return matches
}

function isLikelySpam(text: string | null): boolean {
  if (!text) return false

  const t = text.toLowerCase()
  const spamSignals = [
    'http://',
    'https://',
    'www.',
    '.com',
    'dm me',
    'promote it',
    'followers',
    'crypto',
    'bitcoin',
  ]

  return spamSignals.some((signal) => t.includes(signal))
}

function inferContentType(raw: unknown): ContentType {
  const text = JSON.stringify(raw).toUpperCase()

  if (
    text.includes('REEL') ||
    text.includes('REELS') ||
    text.includes('MEDIA_PRODUCT_TYPE":"REELS') ||
    text.includes('MEDIA_PRODUCT_TYPE":"CLIPS')
  ) {
    return 'reel'
  }

  if (text.includes('POST') || text.includes('MEDIA_ID') || text.includes('POST_ID')) {
    return 'post'
  }

  return 'unknown'
}

function buildInsert(
  channel: Channel,
  rawNode: Record<string, unknown>,
  commentId: string,
  postId: string,
  commenterId: string,
  commenterUsername: string | null,
  commentText: string,
): CommentEventInsert {
  const normalized = normalizeText(commentText)
  const matchedKeywords = detectKeywords(normalized)
  const spam = isLikelySpam(commentText)

  return {
    channel,
    content_type: inferContentType(rawNode),
    post_id: postId,
    comment_id: commentId,
    commenter_platform_user_id: commenterId,
    commenter_username: commenterUsername,
    comment_text: commentText,
    comment_text_normalized: normalized,
    matched_keywords: matchedKeywords,
    keyword_detected: matchedKeywords[0] ?? null,
    is_spam: spam,
    should_send_dm: false,
    dm_sent: false,
    dm_sent_at: null,
    status: spam
      ? 'ignored_spam'
      : matchedKeywords.length > 0
      ? 'eligible'
      : 'ignored_no_keyword',
    raw_webhook_payload: rawNode,
  }
}

function extractInstagramCommentRows(payload: Record<string, unknown>): CommentEventInsert[] {
  const rows: CommentEventInsert[] = []
  const entry = Array.isArray(payload.entry) ? payload.entry : []

  for (const e of entry) {
    if (!e || typeof e !== 'object') continue

    const entryObj = e as Record<string, unknown>
    const changes = Array.isArray(entryObj.changes) ? entryObj.changes : []

    for (const change of changes) {
      if (!change || typeof change !== 'object') continue

      const changeObj = change as Record<string, unknown>
      const field = typeof changeObj.field === 'string' ? changeObj.field : null
      if (field !== 'comments') continue

      const value =
        changeObj.value && typeof changeObj.value === 'object'
          ? (changeObj.value as Record<string, unknown>)
          : null
      if (!value) continue

      const commentId =
        typeof value.id === 'string'
          ? value.id
          : typeof value.comment_id === 'string'
          ? value.comment_id
          : null

      const postId =
        typeof value.media_id === 'string'
          ? value.media_id
          : typeof value.post_id === 'string'
          ? value.post_id
          : typeof entryObj.id === 'string'
          ? entryObj.id
          : 'unknown'

      const from =
        value.from && typeof value.from === 'object'
          ? (value.from as Record<string, unknown>)
          : null

      const commenterId =
        typeof from?.id === 'string'
          ? from.id
          : typeof value.from_id === 'string'
          ? value.from_id
          : 'unknown'

      const commenterUsername =
        typeof from?.username === 'string'
          ? from.username
          : typeof value.username === 'string'
          ? value.username
          : null

      const commentText =
        typeof value.text === 'string'
          ? value.text
          : typeof value.message === 'string'
          ? value.message
          : null

      if (!commentId || !commentText) continue

      rows.push(
        buildInsert(
          'instagram',
          { entry: entryObj, change: changeObj },
          commentId,
          postId,
          commenterId,
          commenterUsername,
          commentText,
        ),
      )
    }
  }

  return rows
}

function extractFacebookCommentRows(payload: Record<string, unknown>): CommentEventInsert[] {
  const rows: CommentEventInsert[] = []
  const entry = Array.isArray(payload.entry) ? payload.entry : []

  for (const e of entry) {
    if (!e || typeof e !== 'object') continue

    const entryObj = e as Record<string, unknown>
    const changes = Array.isArray(entryObj.changes) ? entryObj.changes : []

    for (const change of changes) {
      if (!change || typeof change !== 'object') continue

      const changeObj = change as Record<string, unknown>
      const field = typeof changeObj.field === 'string' ? changeObj.field : null
      if (field !== 'feed') continue

      const value =
        changeObj.value && typeof changeObj.value === 'object'
          ? (changeObj.value as Record<string, unknown>)
          : null
      if (!value) continue

      const item = typeof value.item === 'string' ? value.item : null
      const verb = typeof value.verb === 'string' ? value.verb : null
      if (item !== 'comment' || verb !== 'add') continue

      const commentId =
        typeof value.comment_id === 'string'
          ? value.comment_id
          : typeof value.id === 'string'
          ? value.id
          : null

      const postId =
        typeof value.post_id === 'string'
          ? value.post_id
          : typeof value.parent_id === 'string'
          ? value.parent_id
          : typeof entryObj.id === 'string'
          ? entryObj.id
          : 'unknown'

      const senderId =
        typeof value.sender_id === 'string'
          ? value.sender_id
          : value.from &&
            typeof value.from === 'object' &&
            typeof (value.from as Record<string, unknown>).id === 'string'
          ? ((value.from as Record<string, unknown>).id as string)
          : 'unknown'

      const senderUsername =
        value.from &&
        typeof value.from === 'object' &&
        typeof (value.from as Record<string, unknown>).name === 'string'
          ? ((value.from as Record<string, unknown>).name as string)
          : null

      const commentText =
        typeof value.message === 'string'
          ? value.message
          : typeof value.text === 'string'
          ? value.text
          : null

      if (!commentId || !commentText) continue

      rows.push(
        buildInsert(
          'facebook',
          { entry: entryObj, change: changeObj },
          commentId,
          postId,
          senderId,
          senderUsername,
          commentText,
        ),
      )
    }
  }

  return rows
}

function extractCommentRows(payload: Record<string, unknown>): CommentEventInsert[] {
  const objectType = typeof payload.object === 'string' ? payload.object : null

  if (objectType === 'instagram') return extractInstagramCommentRows(payload)
  if (objectType === 'page') return extractFacebookCommentRows(payload)

  return [...extractInstagramCommentRows(payload), ...extractFacebookCommentRows(payload)]
}

Deno.serve(async (req) => {
  try {
    const url = new URL(req.url)

    if (req.method === 'GET') {
      const mode = url.searchParams.get('hub.mode')
      const token = url.searchParams.get('hub.verify_token')
      const challenge = url.searchParams.get('hub.challenge')

      if (mode === 'subscribe' && token === META_WEBHOOK_VERIFY_TOKEN && challenge) {
        return new Response(challenge, { status: 200 })
      }

      return new Response('Forbidden', { status: 403 })
    }

    if (req.method !== 'POST') {
      return new Response('Method Not Allowed', { status: 405 })
    }

    const payload = (await req.json()) as Record<string, unknown>
    const rows = extractCommentRows(payload)

    if (rows.length === 0) {
      return json({
        ok: true,
        inserted: 0,
        message: 'Webhook received, no recognizable comment events extracted yet.',
      })
    }

    const { error } = await supabase
      .from('comment_events')
      .upsert(rows, { onConflict: 'comment_id', ignoreDuplicates: false })

    if (error) {
      console.error('Supabase insert error:', error)
      return json({ ok: false, inserted: 0, error: error.message }, 500)
    }

    return json({ ok: true, inserted: rows.length })
  } catch (error) {
    console.error('meta-webhook fatal error:', error)
    return json(
      {
        ok: false,
        error: error instanceof Error ? error.message : 'Unknown error',
      },
      500,
    )
  }
})
