import scrapy


class LxfSpider(scrapy.Spider):
    name = "lxf"
    allowed_domains = ["linuxformat.com"]
    start_urls = ["https://linuxformat.com"]

    def parse(self, response):
        pass
