# LegalEase - AI-Powered Legal Document Generator

Generate employment contracts, NDAs, lease agreements and more from a few inputs.
Edit the result in the browser and download it as **.txt**, **.docx** (logo, Times New Roman,
key-terms table, footer) or **.pdf** (logo header and footer on every page).

**Stack:** FastAPI (backend) | Streamlit (website / frontend) | Google Gemini | python-docx | fpdf2

```
LegalEase/
  ai_core/
    gemini_generator.py   Gemini prompt + generation (offline template if no API key)
    generator.py          sanitize_text, format_docx, format_pdf, format_html_preview
    text_utils.py         text cleaning and parsing helpers
  frontend/app.py         Streamlit website
  legalEaseAPI/
    main.py               FastAPI app (/, /health)
    routes.py             POST /generate
  Image/                  Logo.png, inverseLogo.png
  tests/                  pytest tests
  tools/make_logo.py      regenerates the logos
  config.py  .env  requirements.txt  run.sh  run.bat  Procfile
```

## 1. Prerequisites
- Python 3.10 or newer (https://www.python.org/downloads/) - on Windows tick "Add Python to PATH"
- VS Code (https://code.visualstudio.com/) with the **Python** extension
- A free Gemini API key: https://aistudio.google.com/app/apikey

## 2. Open the project in VS Code
1. Unzip `LegalEase.zip`.
2. VS Code: **File > Open Folder...** and choose the `LegalEase` folder.
3. Open a terminal: **Terminal > New Terminal**.

## 3. Create a virtual environment and install dependencies
Windows (PowerShell):
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```
If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process Bypass` first.

macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
Then press **Ctrl+Shift+P > Python: Select Interpreter** and pick the one inside `venv`.

## 4. Add your Gemini API key
Open the `.env` file and replace the placeholder:
```
GEMINI_API_KEY=paste_your_real_key_here
```
Without a key the app still runs using a built-in offline template, so you can test the whole
flow (preview, edit, downloads) first.

The project brief names `gemini-1.5-pro`. Google has retired the 1.5 models, so the default is
`gemini-2.5-flash`, with fallbacks. Change it with `GEMINI_MODEL=...` in `.env` if you prefer
another model available to your key.

## 5. Run the app
Use **two terminals** (Terminal > Split Terminal, activate `venv` in both).

Terminal 1 - backend:
```bash
uvicorn legalEaseAPI.main:app --reload
```
Terminal 2 - website:
```bash
streamlit run frontend/app.py
```
Open **http://localhost:8501**. The API docs are at http://localhost:8000/docs.

One-command alternative: `run.bat` (Windows) or `./run.sh` (macOS/Linux).

## 6. Test it
1. In the website click **Freelance Contract** to load example data, then **Generate Document**.
2. Check the preview, click **Click to Edit Document**, change some text (Ctrl+Enter applies).
3. Download the **.TXT**, **.DOCX** and **.PDF** and open each: the logo, key-terms table and footer
   should be there, and your edits should appear in all three.
4. The sidebar shows whether the backend is online and whether Gemini or the offline template is used.

Automated tests:
```bash
pip install -r requirements-dev.txt
pytest -v
```

## Troubleshooting
- **"Cannot reach the backend"** - start Terminal 1 first; the site expects http://localhost:8000 (change with `BACKEND_URL` in `.env`).
- **"All Gemini models failed"** - the message lists each model's error. Usually a wrong API key, no quota, or a model name your key cannot access; set `GEMINI_MODEL` in `.env`.
- **ModuleNotFoundError** - the venv is not active, or run `pip install -r requirements.txt` again.
- **PDF shows `?`** - PDF export uses Latin characters only; use DOCX or TXT for other scripts.
- Edited `.env`? Restart the backend.

## Deployment
Backend: any host that runs `uvicorn` (Render, Railway, Fly.io, VPS) - the `Procfile` is included; set `GEMINI_API_KEY` as an environment variable.
Frontend: Streamlit Community Cloud with `frontend/app.py`, and set `BACKEND_URL` to your deployed backend URL.

## Disclaimer
LegalEase generates AI drafts, not legal advice. Have every document reviewed by a qualified attorney before use.
