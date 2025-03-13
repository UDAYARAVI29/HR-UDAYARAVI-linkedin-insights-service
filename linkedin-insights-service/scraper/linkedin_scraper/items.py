import scrapy

class LinkedInPageItem(scrapy.Item):
    page_id = scrapy.Field()
    name = scrapy.Field()
    followers = scrapy.Field()
    industry = scrapy.Field()
    about = scrapy.Field()

class LinkedInPostItem(scrapy.Item):
    post_id = scrapy.Field()
    content = scrapy.Field()
    likes = scrapy.Field()
    comments = scrapy.Field()
    shares = scrapy.Field()
