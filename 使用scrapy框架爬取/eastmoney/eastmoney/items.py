# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EastmoneyItem(scrapy.Item):
    # define the fields for your item here like:
    company_name = scrapy.Field()
    Agu_code = scrapy.Field()
    Agu_brief = scrapy.Field()
    company_brief = scrapy.Field()
    business_scope = scrapy.Field()

