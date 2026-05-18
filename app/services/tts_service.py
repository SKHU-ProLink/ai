import openai
from app.core.config import OPENAI_API_KEY


def generate_tts(text: str) -> bytes:
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text,
    )
    return response.read()
