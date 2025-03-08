import os
import time
from dotenv import load_dotenv
import streamlit as st
import fitz  # PyMuPDF for PDF text extraction
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Limit the number of characters sent to the API
MAX_PDF_TEXT_LENGTH = 5000
MAX_RETRIES = 3  # Number of retries for API requests


def get_gemini_response(input_text, pdf_content, prompt):
    """Fetches a response from Gemini API with retries and timeout handling."""
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    
    for attempt in range(MAX_RETRIES):
        try:
            response = model.generate_content([input_text, pdf_content, prompt])
            return response.text
        except Exception as e:
            st.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff

    return "Error: Unable to get response from Gemini API after multiple attempts."


def input_pdf_setup(uploaded_file, max_chars=MAX_PDF_TEXT_LENGTH):
    """Extracts and limits text from a PDF file."""
    if uploaded_file is not None:
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text_parts = [page.get_text() for page in document]
        pdf_text_content = " ".join(text_parts)
        
        return pdf_text_content[:max_chars]  # Truncate if too long
    else:
        return None


# Streamlit UI setup
st.set_page_config(page_title="Resume Expert")

st.header("JobFit Analyzer")
st.subheader("This Application helps you in your Resume Review")

input_text = st.text_input("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")

submit1 = st.button("Analyze Resume")
submit2 = st.button("Improve My Skills")
submit3 = st.button("Find Missing Keywords")
submit4 = st.button("Check Resume Match Percentage")
input_promp = st.text_input("Custom Query:")
submit5 = st.button("Ask My Query")

# Define prompts
prompts = {
    "analyze": """You are an experienced Technical Human Resource Manager. 
                  Review the resume against the job description and highlight strengths and weaknesses.""",
    "improve_skills": """You are a Technical HR Manager with expertise in data science. 
                         Suggest ways to enhance the candidate's skills based on the job description.""",
    "missing_keywords": """You are an ATS scanner. Identify missing keywords in the resume based on the job description.""",
    "match_percentage": """You are an ATS scanner. Provide a percentage match between the resume and job description, 
                           followed by missing keywords and final thoughts."""
}

if uploaded_file is not None:
    pdf_content = input_pdf_setup(uploaded_file)

    if submit1:
        response = get_gemini_response(input_text, pdf_content, prompts["analyze"])
        st.subheader("Analysis Report")
        st.write(response)

    elif submit2:
        response = get_gemini_response(input_text, pdf_content, prompts["improve_skills"])
        st.subheader("Skill Improvement Suggestions")
        st.write(response)

    elif submit3:
        response = get_gemini_response(input_text, pdf_content, prompts["missing_keywords"])
        st.subheader("Missing Keywords")
        st.write(response)

    elif submit4:
        response = get_gemini_response(input_text, pdf_content, prompts["match_percentage"])
        st.subheader("Resume Match Percentage")
        st.write(response)

    elif submit5 and input_promp.strip():
        response = get_gemini_response(input_text, pdf_content, input_promp)
        st.subheader("Custom Query Response")
        st.write(response)
    elif submit5:
        st.warning("Please enter a query before submitting.")

else:
    st.warning("Please upload a PDF file to proceed.")

