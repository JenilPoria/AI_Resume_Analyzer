from fastapi import APIRouter
# from models import ArticleResponse, ArticleRequest
# from services import get_llm_response
from backend.model.Resume_response import Resume
from backend.model.Resume_request import StateResquest
from backend.service.response_service import get_llm_response
router = APIRouter()

@router.get("/health")
def home():
    return {"message": "FastAPI backend running! our API is healthy"}


@router.post("/process", response_model=Resume)
async def process_article(resume: StateResquest):
    return get_llm_response(resume.resume)
