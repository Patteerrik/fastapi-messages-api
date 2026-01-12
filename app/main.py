from fastapi import FastAPI
from app.routers.messages import router as messages_router

app = FastAPI()

@app.get("/")
def root():
    return {"status":"online"}

app.include_router(messages_router)