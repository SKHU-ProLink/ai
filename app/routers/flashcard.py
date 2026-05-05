from fastapi import APIRouter, HTTPException
from app.schemas.flashcard_schema import FlashcardRequest, FlashcardResponse
from app.services.flashcard_service import generate_flashcards

router = APIRouter()


@router.post("/generate", response_model=FlashcardResponse)
def generate(request: FlashcardRequest):
    try:
        return generate_flashcards(request.level)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
