from fastapi import APIRouter, HTTPException
from app.schemas.sentence_schema import SentenceRequest, SentenceResponse
from app.services.sentence_service import create_sentences

router = APIRouter()


@router.post("", response_model=SentenceResponse)
def generate_sentences(request: SentenceRequest):
    try:
        return create_sentences(request.words, request.level)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
