from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import crud, schemas

router = APIRouter(prefix="/post", tags=["Posts"])

@router.get("/{page_id}", response_model=list[schemas.Post])
def get_posts(page_id: str, db: Session = Depends(get_db)):
    return crud.get_posts_by_page(db, page_id)
