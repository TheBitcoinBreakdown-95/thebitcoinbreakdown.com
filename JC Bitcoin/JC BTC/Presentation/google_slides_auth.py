"""
Google Slides API authentication and connection script.
Uses the shared OAuth credentials from the FreedomLab project.

Usage:
    # Import in your own scripts:
    from google_slides_auth import get_slides_service, get_drive_service

    # Or run directly to test authentication:
    python google_slides_auth.py
"""

import os
import json
from pathlib import Path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# ── Configuration ──────────────────────────────────────────────

# Shared credentials (same Google Cloud project, works across all projects)
CLIENT_SECRET_FILE = str(
    Path.home() / ".config" / "google-drive-mcp"
    / "client_secret_954313044628-ffbe8fkuh7dmbvt3atcb60qopb6eidgm.apps.googleusercontent.com.json"
)

# Shared token file (already authenticated, no browser popup needed)
TOKEN_FILE = str(Path.home() / ".config" / "google-drive-mcp" / "tokens.json")

SCOPES = [
    "https://www.googleapis.com/auth/presentations",
    "https://www.googleapis.com/auth/drive.file",
]


# ── Authentication ─────────────────────────────────────────────

def authenticate():
    creds = None

    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            token_data = json.load(f)

        sec = json.loads(Path(CLIENT_SECRET_FILE).read_text())["installed"]

        creds = Credentials(
            token=token_data.get("access_token"),
            refresh_token=token_data.get("refresh_token"),
            token_uri=sec["token_uri"],
            client_id=sec["client_id"],
            client_secret=sec["client_secret"],
            scopes=SCOPES,
        )

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                print("Token expired. Refreshing...")
                creds.refresh(Request())
            except Exception:
                print("Refresh failed (token revoked). Re-authenticating...")
                creds = None
        if not creds or not creds.valid:
            print("First-time authentication. Your browser will open...")
            flow = InstalledAppFlow.from_client_secrets_file(
                CLIENT_SECRET_FILE, SCOPES
            )
            creds = flow.run_local_server(port=8080)

            # Save token for future use
            os.makedirs(os.path.dirname(TOKEN_FILE), exist_ok=True)
            sec = json.loads(Path(CLIENT_SECRET_FILE).read_text())["installed"]
            token_data = {
                "access_token": creds.token,
                "refresh_token": creds.refresh_token,
                "client_id": sec["client_id"],
                "client_secret": sec["client_secret"],
                "token_uri": "https://oauth2.googleapis.com/token",
                "scope": " ".join(SCOPES),
            }
            with open(TOKEN_FILE, "w") as f:
                json.dump(token_data, f, indent=2)
            print(f"Token saved to: {TOKEN_FILE}")

    return creds


def get_slides_service():
    return build("slides", "v1", credentials=authenticate())


def get_drive_service():
    return build("drive", "v3", credentials=authenticate())


# ── Test ───────────────────────────────────────────────────────

if __name__ == "__main__":
    slides = get_slides_service()
    print("Authenticated and connected to Google Slides API!")
    print("Ready to use. Import this module in your scripts.")
