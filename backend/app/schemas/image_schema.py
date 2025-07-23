from pydantic import BaseModel
from typing import List

class ChatMessage(BaseModel):
    sender: str  # "user" 또는 "assistant"
    message: str

class ImageGenerateRequest(BaseModel):
    messages: List[ChatMessage]

class ImageGenerateResponse(BaseModel):
    emotion: str
    prompt: str
    image_url: str
