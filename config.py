"""Central configuration for LegalEase.

All settings are read from environment variables (optionally from a .env file
in the project root), so the same code runs locally and in the cloud.
"""
import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")


def _clean_key(value: str) -> str:
    """Treat empty values and the .env.example placeholder as 'no key'."""
    value = (value or "").strip().strip('"').strip("'")
    if not value or value.lower().startswith("your_") or value.lower() == "changeme":
        return ""
    return value


# --- Gemini / AI core -------------------------------------------------------
GEMINI_API_KEY = _clean_key(os.getenv("GEMINI_API_KEY", ""))
# The project brief names gemini-1.5-pro. Google has retired the 1.5 family,
# so the default is a current model; override it in .env with GEMINI_MODEL.
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash").strip()
GEMINI_FALLBACK_MODELS = [
    m.strip()
    for m in os.getenv("GEMINI_FALLBACK_MODELS", "gemini-2.5-pro,gemini-2.0-flash").split(",")
    if m.strip()
]
GEMINI_TEMPERATURE = float(os.getenv("GEMINI_TEMPERATURE", "0.4"))
GEMINI_MAX_OUTPUT_TOKENS = int(os.getenv("GEMINI_MAX_OUTPUT_TOKENS", "8192"))
REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "120"))  # seconds

# --- Backend / frontend wiring ----------------------------------------------
BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000").rstrip("/")
BACKEND_HOST = os.getenv("BACKEND_HOST", "0.0.0.0")
BACKEND_PORT = int(os.getenv("BACKEND_PORT", "8000"))

# --- Branding ---------------------------------------------------------------
APP_NAME = "LegalEase"
LOGO_PATH = BASE_DIR / "Image" / "Logo.png"            # dark logo for DOCX / PDF
WEB_LOGO_PATH = BASE_DIR / "Image" / "inverseLogo.png"  # light logo for the dark web UI
FOOTER_TEXT = "LegalEase | AI-generated draft - have it reviewed by a qualified attorney"
