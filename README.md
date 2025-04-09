## lxf_archive

In [issue 309](https://linuxformat.com/archives?issue=309) of LinuxFormat, a scraping tutorial claims to scrape
their archive in only 70 lines of code. Unfortunately, it uses
[Requests](https://requests.readthedocs.io/en/latest/) and
[Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/), fine libraries for making http requests
and parsing HTML, but collectively *NOT* a scraping framework.

Mere parsing of HTML is neither *sufficient* or *necessary* for web-crawling these days.

This repo uses [Scrapy](https://scrapy.org/) to extract the same data in *35* lines of code.

It's not just Scrapy's use of [Xpath](https://docs.scrapy.org/en/latest/topics/selectors.html) that makes it
powerful.

A function-call that makes a request never parses it, so code is flatter by design. It's easier for novices
to avoid bad code.

Want to be kind to your victims?
[Enable Autothrottle.](https://docs.scrapy.org/en/latest/topics/autothrottle.html)

Save the data to a .csv with:

```bash
scrapy crawl lxf -o lxf_archive.csv 
```

(Or, save in .json format, or push to AWS S3, Scrapy does these things out-of-the-box.)

Scrapy does things by default that novices don't know they need, and things that experienced
data-miners are too busy to implement.

Need headless-browsers? Try [Playwright](https://pypi.org/project/scrapy-playwright/).

Need tests? Need failures to alert Slack? Try [Spidermon](https://spidermon.readthedocs.io/en/latest/).

Want to easily deploy your spiders? Try [Scrapyd](https://scrapyd.readthedocs.io/en/latest/).

Need to monitor your spiders in real time? Try [Scrapydweb](https://github.com/my8100/scrapydweb).

You want [rotating proxies](https://github.com/TeamHG-Memex/scrapy-rotating-proxies) or
[TOR](https://github.com/8W9aG/scrapy-tor-downloader)? There's a
[Downloader Middleware](https://docs.scrapy.org/en/latest/topics/downloader-middleware.html) for that.

It goes on...

Use the Right Tool for the Right Job.

(Apparently, this was sufficient to make "Letter Of The Month"...)

![LXF LOTM](lxf_letter.png)



