import shutil
from tempfile import NamedTemporaryFile

import whisper

model = whisper.load_model("base")

async def transcribe_with_diarization(file):
    with NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name
    
    # Whisper transcription
    result = model.transcribe(tmp_path)
    
    # Sample JSON output
    return {
        "transcription": result['text'],
        "segments": result.get("segments", []),  # Can include timestamps
        "language": result["language"]
    }
