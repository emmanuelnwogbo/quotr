# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.loader import ItemLoader

from quotes_spider.items import QuotesSpiderItem

number = 0


class QuotesSpider(Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        l = ItemLoader(item=QuotesSpiderItem(), response=response)
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        l.add_value('h1_tag', h1_tag)
        l.add_value('tags', tags)

        return l.load_item()

        # yield {'H1 Tag': h1_tag, 'Tags': tags}

        '''
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            global number
            number += 1
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath(
                './/*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath(
                './/*[@itemprop="keywords"]/@content').extract_first()
            print(
                '\n',
                number,
                '\n',
                text,
                '\n',
                author,
                '\n',
                tags
            )

            yield {
                'Text': text,
                'Author': author,
                'Tags': tags
            }

            next_page_url = response.xpath(
                '//*[@class="next"]/a/@href').extract_first()
            absolute_next_page_url = response.urljoin(next_page_url)
            print(absolute_next_page_url)
            yield scrapy.Request(absolute_next_page_url)

        #res = response.xpath('//a')
        # yield print(res)
        '''
