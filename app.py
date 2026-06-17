from utils.pdf_reader import extract_text_from_pdf
import streamlit as st

# Page configration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered",
)

# Header
st.title("AI Resume Analyzer")

st.markdown(
    """
    Upload your resume and receive AI-powered insights,
    skill extraction, qualification detection, and improvement suggestions.
    """
)

st.divider()

# Features section
st.subheader("📋 What You'll Get")

st.markdown("""
- Resume Summary
- Skills Extracted
- Qualifications Found
- Improvement Suggestions
""")

st.divider()

# File uploader
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    st.success("Resume uploaded successfully!")

    st.subheader("📄 Resume Details")

    st.write(f"File Name: {uploaded_file.name}")

    st.write(f"File Size: {uploaded_file.size / 1024:.2f} KB")

    text = extract_text_from_pdf(uploaded_file)

    st.subheader("📄 Extracted Text")

    st.text_area(
        "Resume Content",
        text,
        height=300
    )