"""
This is a Spyder project to grab most recent news from Bloomberg Markets.
writtenby : duxin
email     : duxn_be@outlook.com
2018 All rights reserved.
"""

import scrapy
from xml.etree.ElementTree import fromstring
#import logging

from scrapy.spiders import SitemapSpider
class MySpider(SitemapSpider):
    #self.log("log1")
    name='myspider'
    #sitemap_urls = ['file:///C://Users/duxin/Codes/source/BloombergMarketsNews/BloombergMarketsNews/data/sitemap.xml']
    sitemap_urls = ['https://www.bloomberg.com/feeds/markets/sitemap_index.xml']
    sitemap_rules = [
        ('/articles/', 'parse2')
    ]
    sitemap_follow = ['/sitemap_recent']

    def parse1(self, response):
        print('a:','absdfasdfasdfasdfasdfsd')
        print('\n\n\n\n')
    
    def parse2(self, response):
        """
        responseURL = response.url
        requestURL = response.request.meta['redirect_urls']
        print('''Response's URL: ''', response.url)
        print('''Request's  URL: ''', response.meta['url'])
        if str(responseURL).__eq__(requestURL):
            pass
        else:
            print('--------------------->>>>>>>>Your request is redirect,retrying.....<<<<<-------------------------')
            yield scrapy.Request(url=requestURL, headers=headers, meta={'url': requestURL}, callback=self.parse)"""
        print('b:',len(response.text))


class GetNewslist(scrapy.Spider):
    name = "spider_newslist"

    def start_requests(self):
        urls = [
            "https://www.bloomberg.com/feeds/markets/sitemap_index.xml",
        ]
        self.article_lists = []
        self.articles = set()
        for url in urls:
            print('Hello World!\n\n\n\n\n\n\n')
            yield scrapy.Request(url=url, callback=self.parse_sitemap)
        print('aaaaaaaaaaaaaaaaaaaaaaaaaa\n\n\n\n\n\n\n')
        for i,url in enumerate(self.article_lists):
            print('progress: %d / %d'%(i, len(self.article_lists)))
            yield scrapy.Request(url=url, callback=self.parse_article_lists)
        self.articles = sorted(list(self.articles), key = lambda x:x[1])
        print(self.articles[-100:])
        print(len(self.articles))

    def parse_sitemap(self, response):
        print(response.status)
        print(len(response.text))
        et = fromstring(response.text)
        for node in et:
            print(node[0].text)
            self.article_lists.append(node[0].text)
        print('Article lists reading finished!')
    
    def parse_article_lists(self, response):
        et = fromstring(response.text)
        for node in et:
            self.articles.add((None, node[1].text.replace('T',' ').replace('Z',''),
                               node[0].text, False))