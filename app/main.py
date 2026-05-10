from fastapi import FastAPI
from dotenv import load_dotenv
from app.routers import flashcard, tts

load_dotenv()

app = FastAPI()


@app.get("/health")
def health_check():
    return {"status": "ok"}


app.include_router(flashcard.router, prefix="/flashcard")
app.include_router(tts.router, prefix="/flashcard/tts")