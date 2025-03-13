from fastapi import FastAPI
from database import engine
from database import models
from routes import page, post, comment, followers

# Initialize database tables
models.Base.metadata.create_all(bind=engine)

# Create FastAPI instance
app = FastAPI(
    title="LinkedIn Insights Microservice",
    description="A FastAPI-based service for LinkedIn page and post insights",
    version="1.0.0"
)

# Include API routes
app.include_router(page.router, prefix="/page", tags=["Page Insights"])
app.include_router(post.router, prefix="/post", tags=["Post Insights"])
app.include_router(comment.router, prefix="/comment", tags=["Comment Insights"])
app.include_router(followers.router, prefix="/followers", tags=["Follower Insights"])

@app.get("/")
def root():
    return {"message": "LinkedIn Insights API is running"}

