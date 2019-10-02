__author__ = "紫羽"


import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs

class Douyu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()

    def testDouyu(self):
        self.driver.get("https://www.douyu.com/directory/all")
        while True:
            soup = bs(self.driver.page_source, "lxml")
            # 房间名, 返回列表
            names = soup.find_all("h3", {"class" : "ellipsis"})
            # 观众人数, 返回列表
            numbers = soup.find_all("span", {"class" :"dy-num fr"})

            # zip(names, numbers) 将name和number这两个列表合并为一个元组 : [(1, 2), (3, 4)...]
            for name, number in zip(names, numbers):
                print ("观众人数: -" + number.get_text().strip() + "-\t房间名: " + name.get_text().strip())

            # 如果在页面源码里找到"下一页"为隐藏的标签，就退出循环
            if self.driver.page_source.find("shark-pager-disable-next") != -1:
                    break

            # 一直点击下一页
            self.driver.find_element_by_class_name("shark-pager-next").click()
        # 测试结束执行的方法
            def tearDown(self):
                # 退出PhantomJS()浏览器
                print ("当前网站直播人数" + str(self.num))
                print ("当前网站观众人数" + str(self.count))
                self.driver.quit()

if __name__ == '__main__':
    unittest.main()