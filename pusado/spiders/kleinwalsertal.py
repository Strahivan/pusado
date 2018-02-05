# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class kleinwalsertal(CrawlSpider):

    name = 'kleinwalsertal'
    allowed_domains = ['kleinwalsertal.com']
    start_urls = ['https://www.kleinwalsertal.com/de/suchen-und-buchen/unterkuenfte/suche/liste?from=&to=&categories%5B%5D=&a0=2&c0=0']


    # First xPath-link is for click - to open detailed-view
    # Second xPath-link is to change sites (page 1 of 10), (page 2 of 10)

    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="demi-list-filter"]/div/div/div/div[1]/div/div/div[3]/div/div/div/div[2]/a[1]', '//*[@id="demi-pagination-container"]/div/div/ul/li/a'))
    ,callback="parse_items", follow=True),)


    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="demi-map-address-container"]/div[1]/strong/text()').extract()
           item ["email"] = hxs.select('//*[@id="demi-map-address-container"]/div[2]/a[1]/@href').extract()
           items.append(item)
           return items


