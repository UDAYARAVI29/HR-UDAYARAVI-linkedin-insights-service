import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "")
    REDIS_URL = os.getenv("REDIS_URL", "")
    LINKEDIN_API_KEY = os.getenv("LINKEDIN_API_KEY", "")
config = Config()
