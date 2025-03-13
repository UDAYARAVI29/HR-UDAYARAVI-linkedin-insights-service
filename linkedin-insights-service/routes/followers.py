from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import crud, schemas

router = APIRouter(prefix="/followers", tags=["Followers"])

@router.get("/{page_id}", response_model=list[schemas.SocialMediaUser])
def get_followers(page_id: str, db: Session = Depends(get_db)):
    return crud.get_followers_by_page(db, page_id)
