LinkedIn Insights Microservice
Overview
This project is a LinkedIn Insights Microservice that allows users to fetch and analyze LinkedIn page insights using a scraper-based approach (or API if applicable). The system stores data in a database and provides RESTful endpoints to retrieve page details, followers, posts, and more.

Features
Mandatory Requirements Implemented
Scraper Service: Extracts details of any given LinkedIn Page ID, including:

Basic Page Details: Name, URL, LinkedIn ID, Profile Picture, Description, Website, Industry, Total Followers, Head Count, Specialties.
Posts & Comments: Stores the latest 15-25 posts, along with comments.
Employees List: Extracts & stores employee details.
Database Integration: Uses MongoDB/MySQL for persistent storage with proper relationships between entities.

RESTful API Endpoints:

Get LinkedIn Page Details by ID.
Filter Pages by Follower Count, Industry, Name (similar search).
Get list of Followers/Following of a Page.
Retrieve Recent Posts (10-15 latest posts).
Pagination for large datasets.
 Postman Collection: A fully tested Postman collection is provided for easy API testing.

Bonus Features Implemented
AI-Powered Summary: Generates an AI summary of a Page using Gemini API based on its followers, type, and activities.

Asynchronous Processing: Uses async programming for scraping, database operations, and API requests to improve performance.

Cloud Storage (S3): Saves profile pictures & post images to Amazon S3 and retrieves them via a CDN.

Caching (Redis): Implements data caching with a TTL of 5 minutes to optimize frequent API calls.

Dockerization: The entire application is Dockerized for easy deployment.

Technology Stack
Backend Framework: FastAPI 
Database: postgresql
Scraper: BeautifulSoup / Scrapy / Selenium
Caching: Redis
Cloud Storage: AWS S3 
Containerization: Docker

Conclusion
This project provides a scalable, efficient, and AI-powered LinkedIn insights microservice with robust scraping, database storage, and API endpoints. It meets all mandatory requirements and includes bonus features for enhanced performance.

Submitted By: HR UDAYARAVI
Date: 13.03.2025