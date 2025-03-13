import pymongo

DB_NAME = "linkedin_insights"

COLLECTIONS = {
    "linkedin_pages": [
        {"name": "Example Company", "page_id": "123456", "followers": 10000, "industry": "Tech"},
    ],
    "linkedin_posts": [
        {"post_id": "987654", "content": "This is a sample post!", "likes": 100, "comments": 20, "shares": 5},
    ]
}

def init_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client[DB_NAME]

    for collection_name, sample_data in COLLECTIONS.items():
        collection = db[collection_name]
        if collection.count_documents({}) == 0:
            collection.insert_many(sample_data)
            print(f"Initialized collection: {collection_name}")

    print("Database initialization complete.")

if __name__ == "__main__":
    init_db()
