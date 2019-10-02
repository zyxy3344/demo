__author__ = "紫羽"

from Spider.Spider import base
from lxml import etree

import threading
import queue

import requests
import json
class ThreadCrawl(threading.Thread):
    def __init__(self, threadName, pageQueue, dataQueue):
        super(ThreadCrawl, self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue

    def run(self):
        while not CRAWL_EXIT:
            try:
                page = self.pageQueue.get(False)
                url = 'https://www.qiushibaike.com /8hr/page/' +  str(page) + '/'
                content = base.loadpage(url)
                self.dataQueue.put(content)
            except:
                pass

CRAWL_EXIT = False
PARSE_EXIT = False
def main():
        pageQueue = queue.Queue(10)
        # 页码队列
        for i in range(1,11):
            pageQueue.put(i)
        dataQueue = queue.Queue()

        crawlList = ["采集线程1号","采集线程2号","采集线程3号"]
        for threadName in crawlList:
            thread = ThreadCrawl(threadName, pageQueue, dataQueue)
            thread.start()
            threadcrawl.append
if __name__ == '__main__':
    main()
