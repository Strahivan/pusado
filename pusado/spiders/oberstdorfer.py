# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class Oberstdorfer(CrawlSpider):

    name = 'oberstdorfer'
    allowed_domains = ['wir-oberstdorfer.de']
    start_urls = ['http://www.wir-oberstdorfer.de/gastgeber/gastgeberverzeichnis.html']


    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="results-list"]/div', '//*[@id="results-list"]/div[1]/section/div/div[2]/div[8]/div[1]/div'))
    ,callback="parse_items", follow=True),)

    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="detail-kontakt"]/div/div[1]/div/text()[1]').extract()
           item ["email"] = hxs.select('//*[@id="detail-kontakt"]/div/div[2]/a[2]/@href').extract()
           item ["website"] = hxs.select('//*[@id="detail-kontakt"]/div/div[2]/a[1]/@href').extract()
           items.append(item)
           return items


#//*[@id="results-list"]/div
#//*[@id="results-list"]/div/section/div/div[3]/div[2]/h2/a
