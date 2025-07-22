from fastapi import APIRouter
from app.schemas.chat_schema import ChatMessage
from app.storage.chat_log import append_chat_log
from app.services.gpt_chat import get_gpt_response

router = APIRouter(prefix="/chat", tags=["Chat"])  

@router.post("/send")
async def receive_message(message: ChatMessage):
    append_chat_log(message.dict())
    return {"status": "received"}

@router.post("/reply")
async def chat_reply(message: ChatMessage):
    messages = [
        {"role": "system", "content": "당신은 사용자와 감정을 이해하려 노력하는 상담자입니다."},
        {"role": message.role, "content": message.content}
    ]
    gpt_reply = get_gpt_response(messages)
    return {"role": gpt_reply["role"], "content": gpt_reply["content"]}
