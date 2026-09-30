@echo off
REM Starts the FastAPI backend and the Streamlit frontend (Windows).
cd /d "%~dp0"
if exist venv\Scripts\activate.bat call venv\Scripts\activate.bat
start "LegalEase Backend" cmd /k uvicorn legalEaseAPI.main:app --port 8000
timeout /t 3 >nul
streamlit run frontend/app.py
