# -*- coding: utf-8 -*-

import scrapy


class MadoItem(scrapy.Item):
    path = scrapy.Field()
    url = scrapy.Field()
    size = scrapy.Field()
