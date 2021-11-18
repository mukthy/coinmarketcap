# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
# from scrapy_cloudflare_middleware.middlewares import CloudFlareMiddleware


class CoinmarketSpider(CrawlSpider):
    name = 'coinmarket'
    allowed_domains = ['coinmarketcap.com']
    start_urls = ['https://coinmarketcap.com/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//tbody/tr/td/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths="(//li[@class='next']/a)[2]"))
    )

    def parse_item(self, response):
        yield {
            'Name': response.xpath("//h2[@class='sc-1q9q90x-0 jCInrl h1']/text()").get(),
            'Rank': response.xpath("//div[@class='namePill namePillPrimary']/text()").get(),
            'Price(USD)': response.xpath("//div[@class='priceValue ']/text()").get()
        }

