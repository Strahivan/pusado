# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class Saalbach(CrawlSpider):

    name = 'saalbach'
    allowed_domains = ['saalbach.com']
    start_urls = ['https://www.saalbach.com/saalbach-booking/Query?AR=1&FL=100&LG=0&RA=2&AM=1']

    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=())
    ,callback="parse_items", follow=True),)

    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="resultList"]/div/div/div[2]/div[1]/div[2]/div[1]/h4/text()').extract()
           item ["email"] = hxs.select('//*[@id="resultList"]/div/div/div[2]/div[2]/div/div[2]/a/@href').extract()
           item ["website"] = hxs.select('//*[@id="resultList"]/div/div/div[2]/div[2]/div/div[3]/a/@href').extract()
           items.append(item)
           return items

