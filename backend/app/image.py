from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

router = APIRouter()

class Message(BaseModel):
    sender: str
    text: str

class ImageRequest(BaseModel):
    messages: List[Message]

@router.post("/generate-image")
async def generate_image(request: ImageRequest):
    try:
        conversation = "\n".join([f"{msg.sender}: {msg.text}" for msg in request.messages])

        # 1. 감정 분석
        emotion_prompt = f"""다음 대화의 전반적인 감정을 한 단어로 요약해 주세요. 예: 행복, 슬픔, 분노, 놀람 등\n\n{conversation}"""
        emotion_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": emotion_prompt}]
        )
        emotion = emotion_response.choices[0].message.content.strip()

        # 2. 이미지 프롬프트 생성
        image_prompt = f"A digital art representation of the emotion: {emotion}"

        # 3. DALL·E 이미지 생성
        image_response = client.images.generate(
            model="dall-e-3",
            prompt=image_prompt,
            size="1024x1024",
            quality="standard",
            n=1
        )
        image_url = image_response.data[0].url
        return {"emotion": emotion, "image_url": image_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
