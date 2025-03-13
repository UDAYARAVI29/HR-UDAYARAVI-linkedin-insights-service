import scrapy
from linkedin_scraper.items import LinkedInPostItem

class LinkedInPostsSpider(scrapy.Spider):
    name = "linkedin_posts"
    allowed_domains = ["linkedin.com"]
    start_urls = ["https://www.linkedin.com/company/example/posts/"]

    def parse(self, response):
        posts = response.css(".post")

        for post in posts:
            item = LinkedInPostItem()
            item["post_id"] = post.css("::attr(data-id)").get()
            item["content"] = post.css(".content::text").get()
            item["likes"] = post.css(".likes::text").get()
            item["comments"] = post.css(".comments::text").get()
            item["shares"] = post.css(".shares::text").get()
            yield item
