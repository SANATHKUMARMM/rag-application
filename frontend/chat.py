import os

import dotenv
import requests
import gradio

dotenv.load_dotenv(override=True)

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost")
BACKEND_PORT = os.getenv("BACKEND_PORT", "8080")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost")
FRONTEND_PORT = os.getenv("FRONTEND_PORT", "7860")


def send_chat_message(message: str,history) -> str:
    response = requests.post(url=f"{BACKEND_URL}:{BACKEND_PORT}", json={"message": message})
    return response.json()["message"]


gradio.ChatInterface(send_chat_message).launch(
    server_name=FRONTEND_URL,
    server_port=int(FRONTEND_PORT)
)