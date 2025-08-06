import argparse
import os
import time
import pdfplumber
from topic_extraction.extractor import extract_batch
from generate_toc import generate_docx

def get_text_pages(file_path):
    if file_path.endswith(".pdf"):
        with pdfplumber.open(file_path) as pdf:
            return [page.extract_text() for page in pdf.pages if page.extract_text()]
    elif file_path.endswith(".txt"):
        with open(file_path, encoding="utf-8") as f:
            return [f.read()]
    else:
        raise ValueError("Unsupported file type. Use .pdf or .txt")

def main(file_path, out_path):
    start = time.time()
    print(f"📁 Reading: {file_path}")
    pages = get_text_pages(file_path)

    print(f"🔍 Extracting topics using Gemini (batch mode)...")
    topics = extract_batch(0, pages)

    print(f"📝 Generating TOC to: {out_path}")
    generate_docx(topics, output_path=out_path)

    print(f"✅ Done! Extracted {len(topics)} topics.")
    print(f"⏱️ Total time: {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate TOC from deposition file")
    parser.add_argument("--file", required=True, help="Path to deposition file (.pdf or .txt)")
    parser.add_argument("--out", required=True, help="Path to output TOC (.docx)")

    args = parser.parse_args()
    main(args.file, args.out)
