
# 📘 Deposition Topic Index Generator

A smart LLM-powered pipeline that reads deposition transcripts and auto-generates a clean, chronological Table of Contents (TOC). Designed for paralegals, legal tech teams, and document intelligence workflows.

---

## 🚀 Features

- 🧠 **LLM-Powered Extraction** — Uses Gemini to detect topics with starting page + line numbers
- 📄 **Multiple Output Formats** — Generate TOC in both `.md` and `.docx`
- 🎛️ **Streamlit Interface** — Simple UI for file uploads and TOC previews
- 🔍 **Validation Notebook** — Manual QA support via random sampling

---

## 🗂 File Structure

```

project\_root/
├── app.py                    # Streamlit web app
├── build\_toc.py              # CLI-based TOC generator
├── data/
│   ├── pages/                # Page-wise text chunks
│   ├── uploaded\_input.txt    # Raw extracted text
│   └── topics.json           # Final topic metadata
├── output/
│   ├── toc.md                # Markdown TOC
│   └── toc.docx              # Word-format TOC
├── topic\_extraction/
│   ├── extractor.py          # Gemini-based topic extractor
│   └── prompt\_template.txt   # Reusable prompt template
├── toc\_generator.py          # TOC formatter for .md and .docx
└── validation/
└── validate.ipynb        # Notebook for QA/spot-checks

````

---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/deposition-toc-generator.git
cd deposition-toc-generator

# 2. Install Python dependencies
pip install -r requirements.txt
````

---

## 📦 Dependencies

List for `requirements.txt`:

```txt
streamlit
google-generativeai
python-docx
docx
pandas
```

Also recommended:

```bash
pip install openpyxl matplotlib numpy pandas ipykernel
```

---


## 🧪 How to Use

### 🖥️ Run with Streamlit UI

```bash
streamlit run app.py
```

Upload your transcript and get an instant TOC.

---

## 🏛️ Ideal For

* ⚖️ Law firms digitizing deposition archives
* 🧠 Legal tech teams building smarter document tools
* 🏢 In-house compliance & litigation teams automating review

---

## 📬 Contact

Built by **Abhishek**



Let me know if you want this turned into a full GitHub template repo with starter commits, issues, and contribution guides.
```
