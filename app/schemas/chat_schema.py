from pydantic import BaseModel
from typing import Literal

class ChatMessage(BaseModel):
    user_id: str
    role: Literal["user", "assistant"]
    content: str
