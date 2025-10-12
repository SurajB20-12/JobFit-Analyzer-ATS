# JobFit Analyzer

## Application link: https://jobfit-analyzer-ats-eflb46hwzvmyze9a8nsglc.streamlit.app/

JobFit Analyzer is a Streamlit web application that helps you analyze and improve your resume by comparing it with a job description. It uses the Groq Cloud API (Llama 3 model) via LangChain for advanced natural language processing.

---

## Features

- **Resume Analysis:** Get strengths and weaknesses of your resume for a specific job.
- **Skill Improvement Suggestions:** Receive tailored advice to enhance your skills.
- **Missing Keywords:** Identify important keywords missing from your resume.
- **Resume Match Percentage:** See how well your resume matches the job description.
- **Custom Queries:** Ask any question about your resume and job fit.

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/SurajB20-12/JobFit-Analyzer-ATS.git
cd jobfit-analyzer
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit python-dotenv pymupdf langchain langchain-groq
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

**Note:**

- On Streamlit Cloud, set `GROQ_API_KEY` in the **Secrets** manager, not in `.env`.

### 4. Run the App

```bash
streamlit run app.py
```

---

## Usage

1. Enter the **Job Description** in the provided text box.
2. Upload your **Resume** as a PDF file.
3. Click the desired analysis button:
   - **Analyze Resume**
   - **Improve My Skills**
   - **Find Missing Keywords**
   - **Check Resume Match Percentage**
   - Or enter a **Custom Query**
4. View the results and suggestions in the app.

---

## Deployment

### Local

Just follow the steps above.

### Streamlit Cloud

1. Push your code to GitHub.
2. Deploy on [Streamlit Cloud](https://streamlit.io/cloud).
3. In the app's **Settings → Secrets**, add:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## Requirements

- Python 3.8+
- [Groq API Key](https://console.groq.com/keys)
- PDF resume file

---

## File Structure

```
.
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

## License

MIT License

---

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [LangChain](https://python.langchain.com/)
- [Groq Cloud](https://groq.com/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
