from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.title_generator import generate_titles

router = APIRouter()

class BlogPost(BaseModel):
    content: str

@router.post("/suggest-titles/")
def suggest_titles(post: BlogPost):
    suggestions = generate_titles(post.content)
    return {"titles": suggestions}
