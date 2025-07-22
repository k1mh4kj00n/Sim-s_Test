from pydantic import BaseModel

class AnswerRequest(BaseModel):
    user_id: str
    question_id: int
    answer_text: str

class AnswerResponse(BaseModel):
    status: str
    emotion: str
    image_url: str