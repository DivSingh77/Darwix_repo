from fastapi import APIRouter, File, UploadFile

from app.utils.transcriber import transcribe_audio

router = APIRouter()

@router.post("/transcribe/")
async def transcribe(file: UploadFile = File(...)):
    result = await transcribe_audio(file)
    return result
