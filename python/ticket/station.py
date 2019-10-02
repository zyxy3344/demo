__author__ = "紫羽"

import requests
import re
url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
res = requests.get(url).text
res = re.findall(r"'(.*?)'", res)[0]
res =res.split('@')[1:]
station_info = {}
for item in res:
    con = item.split('|')
    # print(*con)
    station_info[con[1]] = [*con]
station_info = '{}'.format(station_info)
with open('station_info.txt', 'w', encoding='utf-8')as f:
    f.write(station_info)