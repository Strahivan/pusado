# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class Serfaus(CrawlSpider):

    name = 'serfaus'
    allowed_domains = ['serfaus-fiss-ladis.at']
    start_urls = ['https://www.serfaus-fiss-ladis.at/en/accommodations/search-book/liste?sorting=bookable&randSeed=11&timestamp=1517994303&from=07.02.2018&to=31.07.2018&nights=7-10&u0=1&a0=2&c0=']

    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="demi-list-filter"]/ol/li/section/div[3]/div[2]/a[1]','//*[@id="demi-pagination-container"]/div/div/ul/li/a'))
    ,callback="parse_items", follow=True),)



    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="demi-map-address-container"]/div[1]/strong/text()').extract()
           item ["email"] = hxs.select('//*[@id="demi-map-address-container"]/div[2]/a[1]/@href').extract()
           items.append(item)
           return items
