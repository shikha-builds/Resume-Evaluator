from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_suggestions(resume_text, jd_text):

    prompt = f"""
    Analyze this resume against the job description.

    Give ONLY 10 short bullet point suggestions.

    Include:
    1. Missing skills
    2. ATS improvements
    3. Resume enhancement tips
    4. Better action verbs
    5. Formatting improvements

    Keep every point short, clear, and professional.

    Resume:
    {resume_text}

    Job Description:
    {jd_text}
    """

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error generating AI suggestions: {str(e)}"