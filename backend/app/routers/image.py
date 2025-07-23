from fastapi import APIRouter
from app.schemas.image_schema import ImageGenerateRequest, ImageGenerateResponse
from app.services.dalle_gen import analyze_emotion_and_generate_prompt, generate_dalle_image

router = APIRouter()

@router.post("/generate", response_model=ImageGenerateResponse)
def generate_emotion_image(data: ImageGenerateRequest):
    emotion, prompt = analyze_emotion_and_generate_prompt(data.messages)
    image_url = generate_dalle_image(prompt)
    return ImageGenerateResponse(emotion=emotion, prompt=prompt, image_url=image_url)

