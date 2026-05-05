from fastapi import APIRouter, HTTPException, File, Form, UploadFile
from app.schemas.flashcard_schema import FlashcardRequest, FlashcardResponse, PronunciationResponse
from app.services.flashcard_service import generate_flashcards, pronunciation_feedback

router = APIRouter()


@router.post("/generate", response_model=FlashcardResponse)
def generate(request: FlashcardRequest):
    try:
        return generate_flashcards(request.level)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/pronunciation", response_model=PronunciationResponse)
async def pronunciation(
    audio_file: UploadFile = File(...),
    target_word: str = Form(...),
):
    try:
        return await pronunciation_feedback(audio_file, target_word)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
