"""
This is a Spyder project to grab most recent news from Bloomberg Markets.
writtenby : duxin
email     : duxn_be@outlook.com
2018 All rights reserved.
"""

import scrapy

class GetNewslist(scrapy.Spider):
    name = "spyder_newslist"

    def start_requests(self):
        urls = [
            "https://www.bloomberg.com/feeds/markets/sitemap_index.xml",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)