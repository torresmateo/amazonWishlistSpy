# -*- coding: utf-8 -*-
import re, urllib2 
from AmazonPriceHTMLParser import *
textfile = file("data.txt", "w")
wishListURL = "http://www.amazon.com/gp/registry/wishlist/12XDZWAFB377I"


website = urllib2.urlopen(wishListURL)
website_html = website.read()

parser = AmazonPriceHTMLParser()
parser.feed(website_html)
textfile.write(website_html)
textfile.close()
