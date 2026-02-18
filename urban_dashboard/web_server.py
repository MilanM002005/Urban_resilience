from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import json
import os

app = FastAPI()

BASE_DIR = r"C:\urban_resilience_ai"
ALERT_FILE = os.path.join(BASE_DIR, "latest_alert.txt")
CHAT_FILE = os.path.join(BASE_DIR, "chat_input.txt")

# serve frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def homepage():
    return FileResponse("static/index.html")

@app.get("/alert")
def get_alert():
    if not os.path.exists(ALERT_FILE):
        return {"status": "No data yet"}

    with open(ALERT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ---- CHAT WITH MCP ----
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "")

    try:
        with open(CHAT_FILE, "w", encoding="utf-8") as f:
            f.write(msg)

        return {"reply": "Message sent to Urban AI. Check Claude agent response."}

    except Exception as e:
        return {"reply": f"Error: {e}"}
