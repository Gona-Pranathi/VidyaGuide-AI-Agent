from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from resume_parser import extract_text
from ai_engine import analyze_resume, chat_with_agent

app = FastAPI(title="VidyaGuide AI Agent")

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "VidyaGuide AI Agent Backend Running"}

@app.post("/analyze-resume/")
async def analyze_resume_api(file: UploadFile = File(...)):
    text = await extract_text(file)
    return analyze_resume(text)

class ChatRequest(BaseModel):
    question: str

@app.post("/chat/")
def chat_api(request: ChatRequest):
    return chat_with_agent(request.question)


