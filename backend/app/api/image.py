from fastapi import APIRouter, Request
from pydantic import BaseModel
from openai import OpenAI

router = APIRouter()

class Message(BaseModel):
    sender: str
    text: str

class ImageRequest(BaseModel):
    messages: list[Message]

@router.post("/generate-image")
async def generate_image(payload: ImageRequest):
    last_user_msg = next((m.text for m in reversed(payload.messages) if m.sender == "user"), "기본 감정")

    client = OpenAI()  # OpenAI key는 환경변수나 client 인자로 설정
    response = client.images.generate(
        prompt=f"'{last_user_msg}'에 어울리는 감정적 분위기의 일러스트",
        model="dall-e-3",
        n=1,
        size="1024x1024"
    )
    return {"image_url": response.data[0].url}
