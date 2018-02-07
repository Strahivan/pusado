# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class Berchtesgaden(CrawlSpider):

    name = 'berchtesgaden'
    allowed_domains = ['berchtesgaden.de']
    start_urls = ['https://www.berchtesgaden.de/hotel-berchtesgaden']


    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="content"]/div[1]/section/section/div/section/article/div[3]/div[2]/a[2]','//*[@id="content"]/div[1]/section/div/section/article/div[3]/div[2]/a[2]','//*[@id="host_searchForm"]/div/div[3]/ul/li/a'))
    ,callback="parse_items", follow=True),)

    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="content"]/div[1]/section/div/aside/div/div[4]/div[1]/div[2]/div[1]/div/span[1]/text()').extract()
           item ["email"] = hxs.select('//*[@id="content"]/div[1]/section/div/aside/div/div[4]/div[1]/div[2]/div[1]/div/span[7]/a/@href').extract()
           item ["email2"] = hxs.select('//*[@id="content"]/div[1]/section/div/aside/div/div[4]/div[1]/div[2]/div[1]/div/span[6]/a/@href').extract()
           items.append(item)
           return items
#//*[@id="content"]/div[1]/section/div/aside/div/div[4]/div[1]/div[2]/div[1]/div/span[1]/text()
#//*[@id="content"]/div[1]/section/div/aside/div/div[4]/div[1]/div[2]/div[1]/div/span[1]