from fastapi import FastAPI

from app.routers.messages import router as messages_router
from app.database import engine
from app.models import Message, Base
from app.database import Base
from fastapi import Depends
from app.core.security import require_api_key
from app import models


app = FastAPI()


Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"status": "online"}

@app.get("/protected")
def protected(_: str = Depends(require_api_key)):
    return {"status": "ok"}

Base.metadata.create_all(bind=engine)

app.include_router(messages_router)
