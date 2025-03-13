from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from services.scraper import LinkedInScraper
from database import get_db
from database import crud, schemas

router = APIRouter(prefix="/page", tags=["Page"])

@router.get("/{page_id}", response_model=schemas.Page)
def get_page(page_id: str, db: Session = Depends(get_db)):
    db_page = crud.get_page_by_id(db, page_id)
    if db_page:
        return db_page

    scraper = LinkedInScraper()
    page_data = scraper.scrape_page(page_id)
    
    return crud.create_page(db, page_data)
