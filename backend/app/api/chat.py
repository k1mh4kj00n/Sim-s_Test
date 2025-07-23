from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI
import os
from dotenv import load_dotenv

# .env에서 OPENAI_API_KEY 로드
load_dotenv()

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# FastAPI 라우터 생성
router = APIRouter()

# 메시지 스키마 정의
class Message(BaseModel):
    sender: str  # 'user' 또는 'assistant'
    text: str

# 요청 본문 스키마 정의
class ChatRequest(BaseModel):
    messages: List[Message]

# POST /api/chat 엔드포인트
@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # GPT 모델용 메시지 포맷으로 변환
        gpt_messages = [
            {"role": "user" if msg.sender == "user" else "assistant", "content": msg.text}
            for msg in request.messages
        ]

        # GPT 응답 생성
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=gpt_messages
        )

        reply = response.choices[0].message.content.strip()
        return {"response": reply}

    except Exception as e:
        print("❌ 에러:", str(e))
        raise HTTPException(status_code=500, detail=str(e))
