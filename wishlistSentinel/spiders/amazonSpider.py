#!/usr/bin/python
#-*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from wishlistSentinel.items import WishlistSentinelItem


class AmazonSpider(Spider):
    name = "amazonSpider"
    allowed_domains = ["amazon.com"]
    wishlist_url = ''

    def __init__(self, wishlist_url):
        self.wishlist_url = wishlist_url
        self.start_urls = [
            self.wishlist_url
        ]

    def parse(self, response):
        sel = Selector(response)
        items = sel.xpath("//div[starts-with(@id,'itemInfo_')]")
        extraction = []
        for item in items:
            spyItem = WishlistSentinelItem()
            spyItem['title'] = item.xpath(".//a[starts-with(@id,'itemName')]/@title").extract()
            spyItem['price'] = [a.strip() for a in item.xpath(".//span[contains(@class,'a-color-price')][1]/text()").extract()]
            spyItem['link'] = [ "http://www.amazon.com" + str(a) for a in  item.xpath(".//a[starts-with(@id,'itemName')]/@href").extract()]
            extraction.append(spyItem)
        print str(len(items)) + " items extracted"
        return extraction

