import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from pusado.items import PusadoItem

class pusado_crawler(CrawlSpider):

    name = 'pusado'
    allowed_domains = ['hoernerdoerfer.de']
    start_urls = ['https://www.hoernerdoerfer.de/unterkuenfte-allgaeu/0?form=vacancySearch&noDate%5B%5D=true&rooms=1&roomtype=&room0_adults=2&room0_children=0&room0_childAge0=&room0_childAge1=&room0_childAge2=&room0_childAge3=&room1_adults=2&room1_children=0&room1_childAge0=&room1_childAge1=&room1_childAge2=&room1_childAge3=&room2_adults=2&room2_children=0&room2_childAge0=&room2_childAge1=&room2_childAge2=&room2_childAge3=&room3_adults=2&room3_children=0&room3_childAge0=&room3_childAge1=&room3_childAge2=&room3_childAge3=&location=&businesstypes%5B%5D=pension&businesstypes%5B%5D=bauernhof&businesstypes%5B%5D=huette&classification=&endowments=&topics=&name=&sort=&seed=2017112619']

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
