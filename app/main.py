from fastapi import FastAPI
from app.routers.messages import router as messages_router
from app.database import engine
from app.models import Message
from app.database import Base


app = FastAPI()


@app.get("/")
def root():
    return {"status": "online"}

Base.metadata.create_all(bind=engine)

app.include_router(messages_router)
