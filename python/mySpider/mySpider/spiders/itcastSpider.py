__author__ = "紫羽"

import scrapy
from mySpider.items import MyspiderItem

class ItcastSpider(scrapy.Spider):
    # 爬虫名字
    name = 'itcast'
    # 域 允许爬虫作用的范围
    allowd_domains = ["http://www.itcast.cn/"]
    # 爬虫起始url
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    # 方法名不能改
    def parse(self, response):
        # with open('teacher.html', 'wb')as f:
        #     f.write(response.body)
        # teacherItem = []
        teacher_list = response.xpath(r'//div[@class="li_txt"]')
        for each in teacher_list:
            item = MyspiderItem()
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            info = each.xpath('./p/text()').extract()
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            yield item
            # teacherItem.append(item)

