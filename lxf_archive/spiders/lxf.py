
import re

import scrapy

class LxfSpider(scrapy.Spider):
    name = "lxf"
    allowed_domains = ["linuxformat.com"]

    def __init__(self, campaign=None, start=66):
        self.start = start

    def page_request(self, page):
        return scrapy.Request(
            'https://linuxformat.com/archives?issue={}'.format(page),
            meta={'page': page})

    def start_requests(self):
        yield self.page_request(self.start)

    def parse(self, response):
        issue_text = response.xpath('//h2/text()').extract_first()
        base = {
            'issue': int(re.findall('(?<=Issue\s)\d+', issue_text)[0]),
            'month': re.findall('(?<=\()\w+', issue_text)[0],
            'year': int(re.findall('(\d{4})\)', issue_text)[0])
        }

        articles = response.xpath('//h2/following-sibling::div')
        sections = map(str.strip, articles.xpath('preceding-sibling::h2[1]//text()').extract())
        titles = map(str.strip, articles.xpath('h3/text()').extract())
        snippets = map(str.strip, articles.xpath('p/text()[1]').extract())
        authors = (byline[1:-1] for byline in articles.xpath('p/em/text()').extract())
        images = (['https://linuxformat.com'+url] for url in articles.xpath('img/@src').extract())

        fields = ('section', 'title', 'snippet', 'author', 'image_urls')
        article_items = zip(sections, titles, snippets, authors, images)
        yield from ({**base, **dict(zip(fields, item))} for item in article_items)

        if len(articles):
            yield self.page_request(response.meta['page'] + 1)
