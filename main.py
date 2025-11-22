import streamlit as st
import tempfile
import requests
from langchain_community.document_loaders import PyPDFLoader
from nodes.validate_resume_output import validate_resume_output

# Streamlit Frontend

import os

# BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000/process")
BACKEND_URL = "http://127.0.0.1:8000/process"
def main():
    st.title("AI Resume Analyzer")
    st.write("Analyze your resume and get insights on alignment score, suggestions, strengths, weaknesses, and keywords.")

    input_type = st.sidebar.radio("Select input source", ["Text", "PDF"])
    if input_type == "Text":
        resume_text = st.text_area("Paste your resume text below:")
    elif input_type == "PDF":
        resume_text = ""
        resume_file = st.file_uploader("Upload your resume PDF", type=["pdf"])

        if resume_file is not None:
            # Save PDF to a temp file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                temp_file.write(resume_file.read())
                temp_file_path = temp_file.name

            # Load the PDF using LangChain loader
            loader = PyPDFLoader(temp_file_path)
            docs = loader.load()

            if docs:
                resume_text = "\n".join([doc.page_content for doc in docs])
                st.success("Text successfully extracted from PDF.")
                # st.text_area("Extracted Resume Text:", resume, height=300)
            else:
                st.error("No content extracted from the PDF.")


    if st.button("Analyze Resume"):
        if not resume_text.strip():
            st.error("Please enter your resume text before analyzing.")
        else:
            # Run the backend
            with st.spinner("Analyzing your resume..."):
                try:
                    response = requests.post(BACKEND_URL, json={"resume": resume_text, "analysis": None})
                    response.raise_for_status()
                    result  = response.json()
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
                    return

            # Display the analysis
            analysis = validate_resume_output(result)
            # st.write(result)
            st.subheader("Resume Analysis")
  
            st.write(f"**Alignment Score:** {analysis.alignment_score}")
            st.write("**Suggestions:**")
            st.write(", ".join(analysis.suggestions))
            st.write("**Weaknesses:**")
            st.write(", ".join(analysis.weaknesses))
            st.write("**Strengths:**")
            st.write(", ".join(analysis.strengths))
            st.write("**Matched Keywords:**")
            st.write(", ".join(analysis.matched_keywords))
            st.write("**Missing Keywords:**")
            st.write(", ".join(analysis.missing_keywords))

if __name__ == "__main__":
    main()