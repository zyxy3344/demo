__author__ = "紫羽"

import scrapy

from douban.items import DoubanItem

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    offest = 0
    url = 'https://movie.douban.com/top250?start='
    start_urls = [
        # 'http://www.douban.com'
        url + str(offest)
    ]

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath(r'//div[@class="info"]')
        for each in movies:
            # 标题
            item['title'] = each.xpath(r'.//span[@class="title"][1]/text()').extract()[0]

            # 信息
            item['info'] = each.xpath(r'.//div[@class="bd"]/p[1]/text()').extract()[0]

            # 评分
            item['grade'] = each.xpath(r'.//div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]

            # 简介
            # detail = each.xpath(r'.//p[@class="quote"]/span/text()').extract()
            # if detail != 0:
            #     item['detail'] = detail[0]
            yield item

        if self.offest < 225:
            self.offest += 25
        yield scrapy.Request(self.url + str(self.offest), callback=self.parse)
