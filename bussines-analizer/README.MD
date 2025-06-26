Gemini Anonymization Script

This project provides a Python script to anonymize text from multiple sources—plain text files, web pages, and PDF documents—using Google's Gemini 2.0 Flash API.

Features

File Input: Read raw text from a UTF‑8 encoded text file.

Web Scraping: Fetch and extract visible text from any public webpage.

PDF Extraction: Extract text content from PDF files.

Anonymization: Combine all inputs into a single prompt and send to the Gemini API for anonymization.

Output: Write anonymized text to an output file.

Requirements

Dependencies are listed in requirements.txt. You can install them via:

pip install -r requirements.txt

Configuration

API Key: Obtain a Google Cloud API key with access to the Generative Language API.

Environment Variable: Set your key in the script or pass it as an environment variable:

export GEMINI_API_KEY="YOUR_API_KEY_HERE"

Files & URLs:

Prompt file: Prompt1.txt (contains anonymization examples and instructions).

Raw text file: input_teste.txt.

Webpage URL: Set WEBPAGE_URL in the script.

PDF file: Set PDF_FILE in the script.

Usage

python gemini_anon_with_webpdf.py

The script will:

Read the prompt template and raw text.

Fetch and parse the webpage.

Extract text from the specified PDF.

Compile all sources into a combined prompt.

Send to Gemini and save the anonymized output in output.txt.

Customization

Adjust TEMPERATURE for creative vs. deterministic anonymization.

Add retry or logging logic in generate_content() as needed.

Extend to other input sources by following the provided function patterns.

License

MIT © Pedro Martins