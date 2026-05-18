from pydantic import BaseModel
from typing import Literal


class FlashcardRequest(BaseModel):
    level: Literal["EASY", "NORMAL", "HARD"]


class WordItem(BaseModel):
    word: str
    part_of_speech: str
    pronunciation: str
    meaning: str


class FlashcardResponse(BaseModel):
    words: list[WordItem]


class PronunciationResponse(BaseModel):
    is_correct: bool
    recognized_text: str
    feedback: str
