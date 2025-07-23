## backend/app/main.py
from fastapi import FastAPI
from app.routers import chat, image

app = FastAPI()

app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(image.router, prefix="/image", tags=["Image"])

@app.get("/")
def root():
    return {"message": "FastAPI backend running"}
