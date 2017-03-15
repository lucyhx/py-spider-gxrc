# -*- coding: utf-8 -*-
import scrapy


class SearchSpiderSpider(scrapy.Spider):
    name = "search_spider"
    allowed_domains = ["gxrc.com"]
    start_urls = ['http://s.gxrc.com/sJob?schType=1&district=2']

    def parse(self, response):
        pass
