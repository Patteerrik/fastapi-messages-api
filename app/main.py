from fastapi import FastAPI
from app.schemas import Message

app = FastAPI()

@app.get("/")
def root():
    return {"status":"online"}


@app.post("/message")
def create_message(message: Message):
    return {"received_message": message.text
    }