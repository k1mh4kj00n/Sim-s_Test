
from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    role: str  # 예: "user", "assistant"
    content: str

class ImageGenerateRequest(BaseModel):
    chat_history: List[ChatMessage]