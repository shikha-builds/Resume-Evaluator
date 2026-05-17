import os

from google import genai


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def get_ai_suggestions(
    resume_text,
    job_description
):

    prompt = f"""
    You are an ATS resume expert.

    Analyze the following resume
    against the job description.

    Give ONLY 10 short bullet-point
    suggestions to improve the resume.

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text