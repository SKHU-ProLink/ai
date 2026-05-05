from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from app.core.config import OPENAI_API_KEY
from app.schemas.flashcard_schema import FlashcardResponse

LEVEL_DESCRIPTIONS = {
    "EASY": "일상생활에서 자주 쓰이는 쉬운 초등학교 수준",
    "NORMAL": "중학교 교과서에 나오는 중간 난이도",
    "HARD": "고급 어휘로 학문적이거나 전문적인 맥락에서 쓰이는",
}

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 영어 학습 앱을 위한 단어 카드 생성 전문가입니다."),
    ("human", (
        "{level_description} 수준의 영어 단어 5개를 선택하세요. "
        "매번 다양한 단어를 선택하되, 이전에 자주 쓰인 단어는 피하세요.\n\n"
        "반드시 아래 JSON 형식으로만 응답하세요:\n"
        '{{"words": [{{"word": "...", "part_of_speech": "명사/동사/형용사/부사 중 하나", '
        '"pronunciation": "IPA 발음기호", "meaning": "한국어 뜻"}}]}}'
    )),
])

llm = ChatOpenAI(model="gpt-4o-mini", temperature=1.0, api_key=OPENAI_API_KEY)
parser = JsonOutputParser()
chain = prompt | llm | parser


def generate_flashcards(level: str) -> FlashcardResponse:
    result = chain.invoke({"level_description": LEVEL_DESCRIPTIONS[level]})
    return FlashcardResponse(**result)
