import os 
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import time 
import base64
import io
from PIL import Image
import pdf2image
import fitz 
import google.generativeai as genai
#configure genai access Gemini API key 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

MAX_PDF_TEXT_LENGTH = 6000
MAX_RETRIES = 3 

def get_gemini_response(input,pdf_content,prompt):
    model=genai.GenerativeModel('gemini-1.5-pro-latest')
    
    for attempt in range(MAX_RETRIES):
        try:
            response=model.generate_content([input,pdf_content,prompt])
            return response.text
        except Exception as e:
            st.warning(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)




def input_pdf_setup(uploaded_file,max_chars=MAX_PDF_TEXT_LENGTH):
    
    if uploaded_file is not None:
      # Read the PDF file
      document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # Initialize a list to hold the text of each page
      text_parts = []

        # Iterate over the pages of the PDF to extract the text
      for page in document:
          text_parts.append(page.get_text())

      # Concatenate the list into a single string with a space in between each part
      pdf_text_content = " ".join(text_parts)
      return pdf_text_content[:max_chars]
    else:
       raise FileNotFoundError("No file uploaded")

#create streamlit app
st.set_page_config(page_title="Resume Expert")

st.header("JobFit Analyzer")
st.subheader('This Application helps you in your Resume Review')
input_text = st.text_input("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your Resume(PDF)...", type=["pdf"])
pdf_content = ""

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Tell Me About the Resume")

submit2 = st.button("How Can I Improvise my Skills")

submit3 = st.button("What are the Keywords That are Missing")

submit4 = st.button("Percentage match")

input_promp = st.text_input("Queries: Feel Free to Ask here")

submit5 = st.button("Answer My Query")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Review the resume against the job description and highlight strengths and weaknesses.
"""

input_prompt2 = """
You are a Technical HR Manager with expertise in data science. 
Suggest ways to enhance the candidate's skills based on the job description.
"""

input_prompt3 = """
You are an ATS scanner. Identify missing keywords in the resume based on the job description.
"""
input_prompt4 = """
You are an ATS scanner. Provide a percentage match between the resume and job description, 
followed by missing keywords and final thoughts.
"""

if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt3, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt4, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_promp, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")



