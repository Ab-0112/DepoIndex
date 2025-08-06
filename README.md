Perfect—here's the full package, including your directory layout, dependencies, and a clean `README.md` that sets everything up like clockwork:

---

## 📚 `README.md`

```markdown
# 📘 Deposition Topic Index Generator

This project extracts distinct legal topics from deposition transcripts using Gemini LLM and organizes them into a searchable Table of Contents (TOC). Ideal for paralegal review, legal assistants, or document intelligence automation.

---

## 🚀 Features

- LLM-powered topic extraction from transcript pages
- TOC generation in Markdown and Word formats
- Streamlit app for easy upload and processing
- Validation notebook for manual QA sampling

---

## 🗂 File Structure

```
project_root/
├── app.py                    # Streamlit app
├── build_toc.py              # Batch processor script
├── data/
│   ├── pages/                # Page-wise text chunks (e.g., page_5.txt)
│   ├── uploaded_input.txt    # Uploaded raw text
│   └── topics.json           # Final extracted topics
├── output/
│   ├── toc.md                # Markdown TOC
│   └── toc.docx              # Word TOC
├── topic_extraction/
│   ├── extractor.py          # LLM extractor logic
│   └── prompt_template.txt   # Gemini prompt template
├── toc_generator.py          # Markdown/Word TOC generator
└── validation/
    └── validate.ipynb        # Notebook for manual validation
```

---

## ⚙️ Installation

```bash
# Step 1: Clone this repo
git clone https://github.com/your-username/deposition-toc-generator.git
cd deposition-toc-generator

# Step 2: Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Step 3: Install dependencies
pip install -r requirements.txt
```

---

## 📦 Dependencies

Include these in `requirements.txt`:

```txt
streamlit
docx
google-generativeai
python-docx
```

You may also need:

```bash
pip install openpyxl matplotlib numpy pandas ipykernel
```

---

## 🔐 Setup Gemini API Key

```bash
export GEMINI_API_KEY='your-api-key-here'
# or on Windows
set GEMINI_API_KEY=your-api-key-here
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

---

## 📄 Generate TOC Manually

```bash
python build_toc.py
```

---

## ✅ Validate Samples

Open the Jupyter notebook in `validation/validate.ipynb` and run cells to inspect topic extraction output on random pages.

---

## 🏛️ Use Case

This pipeline is ideal for:
- Law firms digitizing and indexing large deposition archives
- Legal AI startups building semantic search tools
- Internal automation at compliance and litigation departments

---

## 📬 Contact

Created by **Abhishek**. If you’d like to collaborate, scale this pipeline, or add auto-segmentation, feel free to reach out!
```

---

Let me know if you’d like a starter GitHub repo template, automated PDF text splitting logic, or a Gemini fallback system. You’ve engineered something incredibly useful—let’s polish it to perfection.
