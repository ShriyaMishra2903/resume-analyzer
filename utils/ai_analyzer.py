import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# Load environment variables from .env
load_dotenv()

# Read Hugging Face token
token = os.getenv("HF_TOKEN")

# Create Hugging Face client
client = InferenceClient(
    provider="auto",
    api_key=token,
)


def analyze_resume(resume_text):
    """
    Sends resume text to the AI model and returns the analysis.
    """

    prompt = f"""
You are an expert HR recruiter.

Analyze the following resume.

Provide:
1. A short professional summary
2. Skills
3. Qualifications
4. Three improvement suggestions

Resume:

{resume_text}
"""

    response = client.chat.completions.create(
        model="Qwen/Qwen2.5-7B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=500,
    )

    return response.choices[0].message.content

