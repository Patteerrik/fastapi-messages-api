from pydantic import BaseModel

class Message(BaseModel):
    text: str

class MessageIn(BaseModel):
    text: str

class MessageOut(BaseModel):
    id:int
    text: str