import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class pusado_crawler(CrawlSpider):

    name = 'pusado'
    allowed_domains = ['hoernerdoerfer.de']
    start_urls = ['https://www.hoernerdoerfer.de/unterkuenfte-allgaeu']

    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="splitScreen__section--list"]'))
    ,callback="parse_items", follow=True),)


    def parse_items(self, response):
           hxs = HtmlXPathSelector(response)
           items = []
           item = PusadoItem()
           item ["name"] = hxs.select('//*[@id="contactSection"]/article/div/p/text()[2]').extract()
           item ["email"] = hxs.select('//*[@id="contactSection"]/article/div/a[2]/@href').extract()
           items.append(item)
           return items
