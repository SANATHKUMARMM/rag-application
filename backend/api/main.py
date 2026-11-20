from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserMessage(BaseModel):
    message: str

@app.post("/")
def chat(user_message: UserMessage):
    return {"message": "Hi"}