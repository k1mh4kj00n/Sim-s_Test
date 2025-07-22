from fastapi import APIRouter
from app.services.dalle_gen import analyze_emotion_and_generate_prompt, generate_dalle_image
from app.schemas.image_schema import ImageGenerateRequest

router = APIRouter()

@router.post("/image/generate")
async def generate_emotion_image(req: ImageGenerateRequest):
    chat_dicts = [{"role": m.role, "content": m.content} for m in req.chat_history]
    emotion, prompt = analyze_emotion_and_generate_prompt(chat_dicts)
    image_url = generate_dalle_image(prompt)
    return {"emotion": emotion, "image_url": image_url}
