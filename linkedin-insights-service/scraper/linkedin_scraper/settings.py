BOT_NAME = "linkedin_scraper"

SPIDER_MODULES = ["linkedin_scraper.spiders"]
NEWSPIDER_MODULE = "linkedin_scraper.spiders"

ROBOTSTXT_OBEY = False  # LinkedIn blocks bots
DOWNLOAD_DELAY = 3
CONCURRENT_REQUESTS = 4

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"

ITEM_PIPELINES = {
    "linkedin_scraper.pipelines.MongoDBPipeline": 300,
}

DOWNLOADER_MIDDLEWARES = {
    "linkedin_scraper.middlewares.UserAgentMiddleware": 400,
}

LOG_LEVEL = "INFO"
