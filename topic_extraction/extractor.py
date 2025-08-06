import os
import re
import time
import docx
import pdfplumber
import google.generativeai as genai
from typing import List, Dict, Optional, Tuple
from concurrent.futures import ThreadPoolExecutor

# 🔑 Gemini setup
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# 🧹 Clean in-text "PAGE ###" lines to avoid model confusion
def clean_transcript_text(page_text: str) -> str:
    text = re.sub(r"(?im)^\s*page\s+\d+\s*$", "", page_text)
    text = re.sub(r"(?i)page\s+\d{2,5}", "[page redacted]", text)
    return text

# 📜 Prompt template (per batch)
PROMPT_TEMPLATE = """
You are an AI legal analyst. Analyze the following **deposition transcript pages** and extract distinct topics introduced.

For each topic, return:
- Topic name
- First **page number and line number** it appears on

⚠️ Only use the provided page range. Ignore any 'Page ###' text in the transcript body — they may be unrelated.

Format:
Topic Name · Page Number · Line Number

Pages:
{{page_text}}

Return a clean list — no extra headers, explanations, or comments.
"""

# 📖 Extract text from PDF
def read_pdf_by_page(file_path: str) -> List[str]:
    with pdfplumber.open(file_path) as pdf:
        return [page.extract_text(layout=True) for page in pdf.pages if page.extract_text()]

# 🧠 Extract from a group of pages (batched)
def extract_batch(start_idx: int, pages: List[str]) -> List[Dict[str, Optional[int]]]:
    page_text = "\n\n".join([
        f"(Page {i+start_idx+1})\n" + clean_transcript_text(p) for i, p in enumerate(pages)
    ])
    prompt = PROMPT_TEMPLATE.replace("{{page_text}}", page_text)

    try:
        response = model.generate_content(prompt)
        output = response.parts[0].text.strip() if response.parts else ""
    except Exception as e:
        print(f"❌ Gemini error on batch starting page {start_idx+1}: {e}")
        return []

    topics = []
    for line in output.splitlines():
        parts = line.strip().split("·")
        if len(parts) == 3:
            topic, page_str, line_str = map(str.strip, parts)
            if page_str.isdigit() and line_str.isdigit():
                topics.append({
                    "topic": topic,
                    "page_start": int(page_str),
                    "line_start": int(line_str)
                })
    return topics

# 🚀 Main processor using batching + threading
def process_file_fast(file_path: str, batch_size: int = 3, max_workers: int = 5) -> List[Dict[str, Optional[int]]]:
    ext = os.path.splitext(file_path)[-1].lower()
    if ext != ".pdf":
        raise ValueError("Only PDF files supported in fast mode")

    pages = read_pdf_by_page(file_path)
    topics_all = []

    def run_batch(start):
        return extract_batch(start, pages[start:start+batch_size])

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(run_batch, i) for i in range(0, len(pages), batch_size)]
        for f in futures:
            result = f.result()
            if result:
                topics_all.extend(result)

    return topics_all

# ✅ Example usage:
# file_path = "example_1.pdf"
# topics = process_file_fast(file_path)
# for t in topics:
#     print(f"{t['topic']}\tPage {t['page_start']}\tLine {t['line_start']}")
