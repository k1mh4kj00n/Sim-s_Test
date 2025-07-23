import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List
from app.schemas.image_schema import ChatMessage

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_emotion_and_generate_prompt(messages: List[ChatMessage]):
    # ChatMessage 객체 리스트를 텍스트로 변환
    content = "\n".join([f"{m.sender}: {m.message}" for m in messages])
    system_prompt = "다음 대화를 기반으로 사용자의 감정을 분석하고, 해당 감정을 묘사할 수 있는 장면을 한 문장으로 설명해줘."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": content},
        ]
    )
    text = response.choices[0].message.content.strip()
    
    # "감정:" 형식을 기준으로 감정과 프롬프트 분리
    if "감정:" in text:
        lines = text.split("\n")
        emotion_line = next((line for line in lines if "감정:" in line), "감정: unknown")
        emotion = emotion_line.replace("감정:", "").strip()
        prompt = "\n".join([line for line in lines if line != emotion_line]).strip()
    else:
        emotion, prompt = "unknown", text

    return emotion, prompt

def generate_dalle_image(prompt: str):
    response = client.images.generate(
        prompt=prompt,
        model="dall-e-3",
        n=1,
        size="1024x1024"
    )
    return response.data[0].url
