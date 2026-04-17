"""Obtiene refresh token para Google Ads API (Installed App OAuth)."""

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/adwords"]

CLIENT_CONFIG = {
    "installed": {
        "client_id": "REDACTED_CLIENT_ID",
        "client_secret": "REDACTED_CLIENT_SECRET",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"],
    }
}

flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
credentials = flow.run_local_server(port=0, open_browser=True)

print("REFRESH TOKEN:")
print(credentials.refresh_token)
