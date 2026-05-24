from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.core.config import OPENAI_API_KEY
from app.schemas.flashcard_schema import WordItem
from app.schemas.sentence_schema import SentenceResponse

LEVEL_DESCRIPTIONS = {
    "EASY": "주어 + 동사 중심의 단순한 문장 구조",
    "NORMAL": "접속사나 전치사구가 포함된 중간 난이도 문장 구조",
    "HARD": "관계절, 분사구문 등이 포함된 복잡한 문장 구조",
}

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 영어 학습 앱을 위한 예문 생성 전문가입니다."),
    ("human", (
        "아래 단어 목록을 보고 각 단어에 맞는 영어 예문과 한국어 해석을 1개씩 생성하세요.\n"
        "문장 난이도: {level_description}\n\n"
        "단어 목록:\n{words}\n\n"
        "반드시 아래 JSON 형식으로만 응답하세요:\n"
        '{{"sentences": [{{"word": "...", "sentence": "...", "meaning": "한국어 해석"}}]}}'
    )),
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.0, api_key=OPENAI_API_KEY)
parser = JsonOutputParser()
chain = prompt | llm | parser


def create_sentences(words: list[WordItem], level: str) -> SentenceResponse:
    words_text = "\n".join(
        f"- {w.word} ({w.part_of_speech}): {w.meaning}" for w in words
    )
    result = chain.invoke({
        "words": words_text,
        "level_description": LEVEL_DESCRIPTIONS[level],
    })
    return SentenceResponse(**result)
