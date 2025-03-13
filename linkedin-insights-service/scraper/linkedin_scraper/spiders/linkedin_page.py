import scrapy
from linkedin_scraper.items import LinkedInPageItem

class LinkedInPageSpider(scrapy.Spider):
    name = "linkedin_page"
    allowed_domains = ["linkedin.com"]
    start_urls = ["https://www.linkedin.com/company/example/"]

    def parse(self, response):
        item = LinkedInPageItem()
        item["page_id"] = response.url.split("/")[-2]
        item["name"] = response.css("h1::text").get()
        item["followers"] = response.css(".followers::text").get()
        item["industry"] = response.css(".industry::text").get()
        item["about"] = response.css(".about-section::text").get()
        yield item
