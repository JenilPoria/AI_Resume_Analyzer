from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI backend running!"}

app.include_router(router)