from pydantic import BaseModel
from typing import Literal
from app.schemas.flashcard_schema import WordItem


class SentenceRequest(BaseModel):
    level: Literal["EASY", "NORMAL", "HARD"]
    words: list[WordItem]


class SentenceItem(BaseModel):
    word: str
    sentence: str
    meaning: str


class SentenceResponse(BaseModel):
    sentences: list[SentenceItem]
