#!/usr/bin/env bash
# Starts the FastAPI backend and the Streamlit frontend (macOS / Linux / Git Bash).
set -e
cd "$(dirname "$0")"
uvicorn legalEaseAPI.main:app --host 0.0.0.0 --port 8000 &
BACKEND_PID=$!
trap 'kill $BACKEND_PID 2>/dev/null' EXIT
sleep 2
streamlit run frontend/app.py
