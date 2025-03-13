from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class LinkedInPageBase(BaseModel):
    name: str
    url: str
    description: Optional[str] = None

class LinkedInPageCreate(LinkedInPageBase):
    pass

class LinkedInPageResponse(LinkedInPageBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class PostBase(BaseModel):
    content: str

class PostCreate(PostBase):
    page_id: int

class PostResponse(PostBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    post_id: int

class CommentResponse(CommentBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
