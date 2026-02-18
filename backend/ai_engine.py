import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

last_resume_context = ""

def analyze_resume(resume_text):
    global last_resume_context

    prompt = f"""
You are a career guidance AI.

Analyze the resume and provide:
- Technical skills
- Skill gaps
- Suitable career roles
- Learning recommendations

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    last_resume_context = response.choices[0].message.content
    return {"analysis": last_resume_context}


def chat_agent(question):
    prompt = f"""
Resume context:
{last_resume_context}

User question:
{question}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"reply": response.choices[0].message.content}





