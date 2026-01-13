from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import MessageIn, MessageOut
from app.models import Message
from app.deps import get_db

router = APIRouter(prefix="/messages", tags=["messages"])

@router.get("", response_model=List[MessageOut])
def read_messages(db: Session = Depends(get_db)):
    return db.query(Message).all()


@router.post("", response_model=MessageOut, status_code=201)
def create_message(message: MessageIn, db: Session = Depends(get_db)
):
    item = Message(text=message.text)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

