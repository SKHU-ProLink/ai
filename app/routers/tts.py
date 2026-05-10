from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from app.schemas.tts_schema import TTSRequest
from app.services.tts_service import generate_tts

router = APIRouter()


@router.post("")
def tts(request: TTSRequest):
    try:
        audio_bytes = generate_tts(request.text)
        return Response(content=audio_bytes, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
