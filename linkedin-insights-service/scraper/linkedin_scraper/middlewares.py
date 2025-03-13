from scrapy import signals
import random

class UserAgentMiddleware:
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
        "Mozilla/5.0 (X11; Linux x86_64)"
    ]

    def process_request(self, request, spider):
        request.headers["User-Agent"] = random.choice(self.USER_AGENTS)

class LinkedInScraperSpiderMiddleware:
    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_spider_output(self, response, result, spider):
        return result
