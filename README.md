 VidyaGuide AI Agent – Career Planning & Resume Mentor
 
 Overview:
-VidyaGuide AI Agent is a Generative and Agentic AI–based career guidance system designed to help students make informed career decisions.
-It analyzes resumes, identifies skills and gaps, recommends suitable career roles, and provides learning guidance through an AI chat agent.

-This project was developed as part of the GenAI Forge Hackathon.

 Problem Statement:
-Many students struggle with career planning due to:
-Lack of personalized guidance
-Generic career advice from existing platforms
-No clear understanding of skill gaps and learning paths
-VidyaGuide AI Agent addresses this by providing resume-based, personalized career recommendations.

 Solution
The system allows users to:
-Upload a resume (PDF)
-Get AI-driven skill analysis and career recommendations
-Identify skill gaps based on industry needs
-Interact with a chat agent for career-related queries

Tech Stack
-Backend: FastAPI (Python)
-Frontend: HTML, CSS, JavaScript
-AI / GenAI: LLM API (via environment variables)
-Resume Parsing: PyPDF2
-API Testing: Swagger UI

 Key Features
-Resume upload and analysis
-Skill identification and gap analysis
-Career role recommendations
-Personalized learning paths
-AI chat agent for career guidance
-Clean and simple UI for easy usage

 Project Structure:
VidyaGuide AI Agent/
│
├── backend/
│   ├── main.py
│   ├── ai_engine.py
│   ├── resume_parser.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── result.html
│   ├── chat.html
│   ├── style.css
│   ├── script.js
│
├── .gitignore
└── README.md

 How to Run the Project:
1️.) Backend Setup
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

2.) Frontend Usage

Open frontend/index.html in a browser
Upload a resume (PDF)
Click Analyze Resume
View results on the results page
Navigate to Chat Agent for queries

 Environment Variables:
API keys are managed using environment variables for security.

Example:
GROQ_API_KEY=your_api_key_here
⚠️ API keys are not committed to GitHub.

 Expected Outcomes:
-Students gain clarity on career paths
-Identification of skill gaps and improvement areas
-Personalized learning recommendations
-Practical application of Generative AI in education
