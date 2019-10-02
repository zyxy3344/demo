__author__ = "紫羽"

import time
import urllib.request as ur
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

class ClassRobbingSystem:

    def __init__(self, username, password):
        self.url = "http://jwgl.ycu.com.cn/login.action"
        self.username = username
        self.password = password

    # 加载页面
    def loadhtml(self):
        options = Options()
        options.add_argument('-headless')  # 无头参数
        driver = Firefox(executable_path='geckodriver', firefox_options=options)  # 配了环境变量第一个参数就可以省了，不然传绝对路径
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        print('1')
        # driver.find_element_by_name("username").send_keys(self.username)
        # driver.find_element_by_name("password").send_keys(self.password)
        # driver.find_element_by_name('captcha_response').send_keys(key)
        driver.save_screenshot('1.png')

    def robbing(self):
        pass


def main():
    t = input("输入抢票的时间段（格式：xxxx-xx-xx 00:00:00）:")
    # 转换成时间数组
    timeArray = time.strptime(t, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    while True:
        if int(time.time()) == timestamp:
            print("8888{0}".format(timestamp))
            print("开始")
            print("结束")
            print("8888{0}".format(time.time()))
            break
        print("时间是：{0},还未开始。".format(int(time.time())))

if __name__ == '__main__':
    S = ClassRobbingSystem('16140851','111111')
    S.loadhtml()