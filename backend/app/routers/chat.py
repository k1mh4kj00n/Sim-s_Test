from fastapi import APIRouter
from app.services.gpt_chat import get_gpt_response
from app.schemas.chat_schema import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/reply", response_model=ChatResponse)
def get_reply(req: ChatRequest):
    reply = get_gpt_response(req.message)
    return ChatResponse(response=reply)