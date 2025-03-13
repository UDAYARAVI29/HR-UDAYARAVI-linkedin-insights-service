import pymongo

class MongoDBPipeline:
    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client["linkedin_scraper"]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        if isinstance(item, dict):
            collection = self.db["linkedin_pages"]
        else:
            collection = self.db["linkedin_posts"]

        collection.insert_one(dict(item))
        return item
