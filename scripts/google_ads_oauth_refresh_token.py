"""Obtiene refresh token para Google Ads API (Installed App OAuth).

Requiere en .env:
  GOOGLE_ADS_CLIENT_ID=...
  GOOGLE_ADS_CLIENT_SECRET=...
"""

import os
from pathlib import Path

from dotenv import load_dotenv
from google_auth_oauthlib.flow import InstalledAppFlow

load_dotenv(Path(__file__).resolve().parent / ".env")

SCOPES = ["https://www.googleapis.com/auth/adwords"]

client_id = os.environ["GOOGLE_ADS_CLIENT_ID"]
client_secret = os.environ["GOOGLE_ADS_CLIENT_SECRET"]

CLIENT_CONFIG = {
    "installed": {
        "client_id": client_id,
        "client_secret": client_secret,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "redirect_uris": ["http://localhost"],
    }
}

flow = InstalledAppFlow.from_client_config(CLIENT_CONFIG, SCOPES)
credentials = flow.run_local_server(port=0, open_browser=True)

print("REFRESH TOKEN:")
print(credentials.refresh_token)
