__author__ = "紫羽"

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json
from bs4 import BeautifulSoup as bs
from Spider.Spider import base
from lxml import etree

# 对象
driver = webdriver.PhantomJS()
driver.get("https://www.huya.com/l")
xml = etree.HTML(driver.page_source)

name_list = xml.xpath(r'//div[@class="box-bd"]/ul/li/span/span/i[@class="nick"]/text()')
name_oline = xml.xpath(r'//div[@class="box-bd"]/ul/li/a[2]/text()')
peoples = xml.xpath(r'//div[@class="box-bd"]/ul/li/span/span[3]/i[2]/text()')
print(name_list)
driver.find_element_by_class_name("laypage_next").click()
a = driver.page_source
print(a)