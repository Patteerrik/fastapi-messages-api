from typing import List

from fastapi import APIRouter

from app.schemas import MessageIn, MessageOut
from app import db

router = APIRouter(prefix="/messages", tags=["messages"])

@router.post("", response_model=List[MessageOut])
def list_messages():
    return db.MESSAGES

@router.post("", response_model=MessageOut, status_code=201)
def create_message(message: MessageIn):
    new_item = {"id": db.NEXT_ID, "text": message.text}
    db.MESSAGES.append(new_item)
    db.NEXT_ID += 1
    return new_item
