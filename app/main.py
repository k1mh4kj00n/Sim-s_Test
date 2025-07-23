from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import chat
from dotenv import load_dotenv
from app.routers import chat, image 
load_dotenv()

app = FastAPI(title="Island-0.0 감정 대화 서비스")

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(chat.router)

app.include_router(image.router)