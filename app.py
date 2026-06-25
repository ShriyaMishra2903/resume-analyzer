import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.ai_analyzer import analyze_resume

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# -----------------------------
# Header
# -----------------------------
st.title("🤖 AI Resume Analyzer")

st.markdown("""
Upload your resume and receive AI-powered insights.

### What You'll Get

- 📄 Professional Summary
- 💻 Skills Extraction
- 🎓 Qualifications
- 💡 Resume Improvement Suggestions
""")

st.divider()

# -----------------------------
# File Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# Process Resume
# -----------------------------
if uploaded_file:

    st.success("✅ Resume uploaded successfully!")

    st.subheader("📄 Resume Details")

    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")

    # Extract text from PDF
    resume_text = extract_text_from_pdf(uploaded_file)

    st.divider()

    st.subheader("📄 Extracted Resume Text")

    st.text_area(
        "Resume Content",
        resume_text,
        height=250
    )

    st.divider()

    st.subheader("🤖 AI Resume Analysis")

    with st.spinner("Analyzing your resume..."):

        analysis = analyze_resume(resume_text)

    st.success("Analysis Complete!")

    st.markdown(analysis)