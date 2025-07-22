from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.main import app

client = TestClient(app)

def test_qna_submit_joy():
    payload = {
        "user_id": "test_user",
        "question_id": 1,
        "answer_text": "정말 행복하고 기뻤어요!"
    }
    response = client.post("/qna/submit", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["emotion"] == "기쁨"
    assert data["image_url"] == "/static/images/기쁨.png"
