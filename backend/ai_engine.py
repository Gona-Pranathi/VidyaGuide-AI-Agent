import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
last_resume_context = ""

def analyze_resume(resume_text: str):
    global last_resume_context

    try:
        prompt = f"""
You are an intelligent career planning AI agent.

Analyze the resume and provide:
- Technical skills identified
- Skill gaps
- Suitable career roles
- Learning recommendations

Resume:
{resume_text[:3000]}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        last_resume_context = response.choices[0].message.content

        return {"analysis": last_resume_context}

    except Exception as e:
        return {"error": str(e)}


def chat_with_agent(user_question: str):
    try:
        prompt = f"""
You are a career guidance AI agent.

Here is the resume analysis context:
{last_resume_context}

Now answer the user's question clearly and helpfully.

User question:
{user_question}
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return {"reply": response.choices[0].message.content}

    except Exception as e:
        return {"error": str(e)}





