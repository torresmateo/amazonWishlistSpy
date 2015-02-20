__author__ = 'torresmateo'

from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from wishlistSentinel.spiders.amazonSpider import AmazonSpider
from scrapy.utils.project import get_project_settings

items = []

def add_item(item):
    items.append(item)

def stop_reactor():
    print "hola"
    reactor.stop()

log.start()
spider = AmazonSpider("http://www.amazon.com/gp/registry/wishlist/12XDZWAFB377I")
settings = get_project_settings()
crawler = Crawler(settings)
crawler.signals.connect(stop_reactor, signal=signals.spider_closed)
crawler.signals.connect(add_item, signal=signals.item_passed)
crawler.configure()
a = crawler.crawl(spider)
crawler.start()
reactor.run() # the script will block here until the spider_closed signal was sent


