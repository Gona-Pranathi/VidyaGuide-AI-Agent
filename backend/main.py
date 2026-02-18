from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from resume_parser import extract_text
from ai_engine import analyze_resume, chat_with_agent

app = FastAPI(title="VidyaGuide AI Agent")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "VidyaGuide AI Agent Backend Running"}


@app.post("/analyze-resume/")
async def analyze_resume_api(file: UploadFile = File(...)):
    text = await extract_text(file)
    result = analyze_resume(text)
    return {"analysis": result}


@app.post("/chat/")
async def chat_api(payload: dict):
    reply = chat_with_agent(payload.get("message", ""))
    return {"reply": reply}