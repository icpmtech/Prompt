````markdown
# Gemini Anonymization Script

A Python tool to anonymize text from multiple sources—plain text files, web pages, and PDF documents—using Google's Gemini 2.0 Flash API.

## Features

- **File Input**: Read raw text from a UTF-8 encoded text file.  
- **Web Scraping**: Fetch and extract visible text from any public webpage.  
- **PDF Extraction**: Extract text content from PDF files.  
- **Anonymization**: Combine all inputs into a single prompt and send to the Gemini API for anonymization.  
- **Output**: Write anonymized text to an output file.  

## Requirements

- Python 3.7+  
- Dependencies listed in `requirements.txt`.

Install dependencies:

```bash
pip install -r requirements.txt
````

## Configuration

1. **API Key**

   * Obtain a Google Cloud API key with access to the Generative Language API.
   * Set your key as an environment variable:

     ```bash
     export GEMINI_API_KEY="YOUR_API_KEY_HERE"
     ```

2. **Environment Variables**
   Rename the file `env.example` to `.env` in the project root and fill in your values:

   ```ini
   GEMINI_API_KEY=YOUR_API_KEY_HERE
   PROMPT_FILE=Prompt1.txt
   RAW_TEXT_FILE=input_teste.txt
   WEBPAGE_URL=https://example.com/page-to-anonymize
   PDF_FILE=document_to_anonymize.pdf
   OUTPUT_FILE=output.txt
   TEMPERATURE=0.0
   ```

## Usage

Run the anonymization script:

```bash
python gemini_anon_with_webpdf.py
```

What happens:

1. Reads the prompt template (`Prompt1.txt`) and raw text (`input_teste.txt`).
2. Fetches and parses the webpage at `WEBPAGE_URL`.
3. Extracts text from the PDF specified by `PDF_FILE`.
4. Compiles all sources into a combined prompt.
5. Sends the prompt to the Gemini API for anonymization.
6. Saves the anonymized output to `OUTPUT_FILE`.

## Customization

* **Temperature**: Adjust the `TEMPERATURE` variable for creative (higher) vs. deterministic (lower) anonymization.
* **Retries & Logging**: Extend or modify the `generate_content()` function to add retry logic or detailed logging.
* **Additional Sources**: Follow the provided function patterns to add other input sources (e.g., database, CSV).

## Development

1. Clone the repository:

   ```bash
   git clone https://github.com/youruser/gemini-anonymization.git
   cd gemini-anonymization
   ```
2. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies and configure `.env`.
4. Run the script as described above.

## License

MIT © Pedro Martins

```
```
