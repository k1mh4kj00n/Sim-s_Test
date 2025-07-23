from fastapi import APIRouter
from app.schemas.qna_schema import AnswerRequest, AnswerResponse
from app.services.emotion import analyze_emotion  # 추가된 부분

router = APIRouter(prefix="/qna", tags=["QnA"])

@router.post("/submit", response_model=AnswerResponse)
async def submit_answer(data: AnswerRequest):
    emotion, image_url = analyze_emotion(data.answer_text)
    return AnswerResponse(
        status="success",
        emotion=emotion,
        image_url=image_url
    )