# -*- coding: utf-8 -*-
import scrapy

from nothing_wrong.items import MadoItem


# Just the metadata, for now
class MetaSpider(scrapy.Spider):
    name = "metaspider"
    allowed_domains = ["manga.madokami.com"]
    start_urls = ["https://manga.madokami.com/"]

    def parse(self, response):
        for row in response.css('#index-table > tbody > tr'):
            a = row.css('td:first-child > a')
            # TODO easier way to extract these things?
            url = response.urljoin(a.xpath('@href').extract()[0])
            path = a.xpath('text()').extract()[0]

            # dirs appended with /
            if path.endswith("/"):
                yield scrapy.Request(url=url, callback=self.parse)
            else:
                size = row.css('td:nth-child(2)') \
                          .xpath('text()').extract()[0].strip()
                yield MadoItem(url=url, path=path, size=size)
