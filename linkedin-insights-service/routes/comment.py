from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from database import crud, schemas

router = APIRouter(prefix="/comment", tags=["Comments"])

@router.get("/{post_id}", response_model=list[schemas.Comment])
def get_comments(post_id: str, db: Session = Depends(get_db)):
    return crud.get_comments_by_post(db, post_id)
