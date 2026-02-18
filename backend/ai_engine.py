import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def analyze_resume(resume_text: str) -> str:
    prompt = f"""
You are a career guidance AI.

Analyze the resume and provide:
- Technical skills
- Skill gaps
- Suitable career roles
- Recommended learning paths

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


def chat_with_agent(message: str) -> str:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are VidyaGuide AI Chat Agent."},
            {"role": "user", "content": message}
        ]
    )

    return response.choices[0].message.content





