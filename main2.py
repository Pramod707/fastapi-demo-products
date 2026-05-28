from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserMessage(BaseModel):
    message: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/chat")
def chat(data: UserMessage):
    return {"reply": f"AI says: {data.message}"}
