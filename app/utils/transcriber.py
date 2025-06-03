import os
import shutil
import tempfile

import whisper
from fastapi import UploadFile

model = whisper.load_model("base")  # Use "small" or "medium" for better results

async def transcribe_audio(file: UploadFile):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    result = model.transcribe(tmp_path)
    os.remove(tmp_path)

    return {
        "transcription": result.get("text"),
        "segments": result.get("segments", []),
        "language": result.get("language")
    }
