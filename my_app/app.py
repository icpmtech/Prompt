import os
from flask import Flask, request, render_template, redirect, url_for, flash
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader

# Load config
load_dotenv()
API_KEY      = os.getenv("API_KEY")
API_URL_BASE = os.getenv("API_URL")
API_URL      = f"{API_URL_BASE}?key={API_KEY}"
TEMPERATURE  = float(os.getenv("TEMPERATURE", 0.0))

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "change-me")

def fetch_webpage_text(url: str) -> str:
    r = requests.get(url); r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    for t in soup(["script", "style"]): t.decompose()
    return soup.get_text(separator="\n").strip()

def extract_pdf_text(file_stream) -> str:
    reader = PdfReader(file_stream)
    return "\n".join(page.extract_text() or "" for page in reader.pages)

def generate_content(prompt: str) -> str:
    body = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": TEMPERATURE},
    }
    resp = requests.post(API_URL, json=body)
    resp.raise_for_status()
    return resp.json()["candidates"][0]["content"]["parts"][0]["text"]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        raw_text = ""
        url = request.form.get("webpage_url", "").strip()
        pdf = request.files.get("pdf_file")
        text_input = request.form.get("raw_text", "").strip()

        if url:
            raw_text += fetch_webpage_text(url) + "\n\n"
        if pdf and pdf.filename:
            raw_text += extract_pdf_text(pdf.stream) + "\n\n"
        if text_input:
            raw_text += text_input

        if not raw_text:
            flash("Please provide at least one source: URL, PDF, or text.")
            return redirect(url_for("index"))

        prompt_base = open(os.getenv("PROMPT_FILE"), encoding="utf-8").read()
        final_prompt = f"{prompt_base}\n\nRaw Text to Anonymize:\n{raw_text}"
        try:
            result = generate_content(final_prompt)
        except Exception as e:
            flash(f"API error: {e}")
            return redirect(url_for("index"))

        return render_template("index.html", output=result, raw_text=raw_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)))