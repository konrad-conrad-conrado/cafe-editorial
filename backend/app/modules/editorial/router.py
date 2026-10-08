from fastapi import APIRouter
from app.modules.editorial.service import load
from app.modules.editorial.schemas import Stories

router = APIRouter(prefix="/stories", tags=["stories"])

@router.get("", response_model=list[Stories])
def stories():
    return load("stories")
