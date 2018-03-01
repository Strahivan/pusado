# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class Garmisch(CrawlSpider):

    name = 'garmisch'
    allowed_domains = ['presiwert-uebernachten.de']
    start_urls = ['https://www.preiswert-uebernachten.de/hotel-pensionen/garmisch-partenkirchen/5042?page=1']


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

# muss manuell gemacht werden da Struktur wie folgt aussieht:
#//*[@id="li-10452"]/div[2]/div/a
#//*[@id="li-15794"]/div[2]/div/a
#//*[@id="li-6745"]/div[2]/div/a
#//*[@id="li-6714"]/div[2]/div/a
#//*[@id="li-10440"]/div[2]/div/a
