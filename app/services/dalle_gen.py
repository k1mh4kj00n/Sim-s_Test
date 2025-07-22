from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_emotion_and_generate_prompt(chat_list: list[dict]) -> tuple[str, str]:
    """
    채팅 목록을 바탕으로 감정 분석과 DALL·E 프롬프트 문장을 생성합니다.
    반환값: (감정, 프롬프트)
    """
    messages = [{"role": "system", "content": "다음 대화에서 사용자의 감정을 분석하고, 그 감정에 어울리는 그림 설명을 한 문장으로 출력하세요. 출력 형식은 '감정, 그림 설명' 형태여야 합니다."}]
    messages += chat_list  # 예: [{"role": "user", "content": "요즘 너무 지쳤어."}]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.7,
        max_tokens=100
    )

    output = response.choices[0].message.content.strip()

    try:
        emotion, prompt = map(str.strip, output.split(",", 1))
    except ValueError:
        emotion, prompt = "기타", "감정을 표현한 풍경 그림"

    return emotion, prompt

def generate_dalle_image(prompt: str) -> str:
    """
    DALL·E를 사용해 이미지 생성 후 URL 반환
    """
    response = client.images.generate(
        model="dall-e-3",  # 또는 "dall-e-2"
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url
