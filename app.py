import streamlit as st
import json
import os
from topic_extraction.extractor import process_file_fast  # ✅ correct batch-based extractor
from generate_toc import generate_markdown, generate_docx

# 🔧 Streamlit page settings
st.set_page_config(page_title="Deposition TOC Generator", layout="centered")
st.title("📘 Deposition Topic Index Generator")

# 📤 File uploader
uploaded_file = st.file_uploader("Upload deposition file (PDF only)", type=["pdf"])

# 🧾 Save uploaded file locally
def save_uploaded_file(file, save_path: str):
    with open(save_path, "wb") as f:
        f.write(file.read())

# 🚀 TOC generation
if st.button("Generate TOC"):
    if uploaded_file:
        filename = uploaded_file.name
        input_path = os.path.join("data", filename)

        with st.spinner("Extracting topics using Gemini..."):
            # 💾 Save file
            save_uploaded_file(uploaded_file, input_path)

            # 🧠 Run Gemini topic extraction with batching + threading
            topics = process_file_fast(input_path, batch_size=3, max_workers=5)

            # 💾 Save JSON output
            with open("data/topics.json", "w", encoding="utf-8") as f:
                json.dump(topics, f, indent=2)

            # 📄 Generate TOC in markdown and docx
            generate_markdown(topics, output_path="output/toc.md")
            generate_docx(topics, output_path="output/toc.docx")

        # ✅ Show success + downloads
        st.success(f"✅ Extracted {len(topics)} topics")
        st.download_button("Download TOC (Markdown)", data=open("output/toc.md").read(), file_name="toc.md")
        st.download_button("Download TOC (Word)", data=open("output/toc.docx", "rb").read(), file_name="toc.docx")
    else:
        st.error("Please upload a valid PDF file.")
