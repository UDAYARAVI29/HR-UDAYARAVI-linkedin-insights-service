from sqlalchemy.orm import Session
from database import models, schemas

def create_page(db: Session, page: schemas.LinkedInPageCreate):
    db_page = models.LinkedInPage(**page.dict())
    db.add(db_page)
    db.commit()
    db.refresh(db_page)
    return db_page

def get_page(db: Session, page_id: int):
    return db.query(models.LinkedInPage).filter(models.LinkedInPage.id == page_id).first()

def get_pages(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.LinkedInPage).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Post).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def get_comments(db: Session, post_id: int):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()
