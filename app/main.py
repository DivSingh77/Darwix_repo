from fastapi import FastAPI

from app.routers import title_suggestion, transcription

app = FastAPI(title="Darwix AI Assignment")

app.include_router(transcription.router, tags=["Transcription"])
app.include_router(title_suggestion.router, tags=["Title Suggestions"])

@app.get("/")
def root():
    return {"message": "Darwix AI Assignment API is working!"}
