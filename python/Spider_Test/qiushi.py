__author__ = "紫羽"
from python.Spider.Spider import base
from bs4 import BeautifulSoup
import json
from lxml import etree


def main():
    html = base.loadpage('https://www.qiushibaike.com/').decode('utf-8')

    xml = etree.HTML(html)

    # 获取所有的节点，返回一个列表
    node_list = xml.xpath(r'//div[contains(@id, "qiushi_tag")]')

    # 遍历节点，在节点下获取每个节点，所需要的内容
    for node in node_list:
        name = node.xpath(r'.//div[@class="author clearfix"]/a/h2/text()|.//div[@class="author clearfix"]/span/h2/text()')[0]
        content = node.xpath(r'string(.//a[@class="contentHerf"]/div/span)')
        print(name)
        print(content)
        pattern = {
            'name': name.strip(),
            'content': content.strip()
        }

        with open('1.json','a+')as f:
            f.write(json.dumps(pattern, ensure_ascii=False))


if __name__ == "__main__":
    main()