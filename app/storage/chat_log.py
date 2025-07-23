import json
from pathlib import Path

LOG_FILE = Path("data/chat_logs.json")
LOG_FILE.parent.mkdir(exist_ok=True)

def append_chat_log(message: dict):
    if LOG_FILE.exists():
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(message)

    with open(LOG_FILE, "w", encoding="utf-8") as f:
        json.dump(logs, f, ensure_ascii=False, indent=2)
