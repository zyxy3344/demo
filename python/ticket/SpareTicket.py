__author__ = "紫羽"

import requests
import json
url = 'https://kyfw.12306.cn/otn/leftTicket/query'
data = {
    'leftTicketDTO.train_date': '2018-07-31', # 时间
    'leftTicketDTO.from_station': 'YIJ',      # 起始站
    'leftTicketDTO.to_station': 'WUJ',        # 终点站
    'purpose_codes': 'ADULT'
}

res = requests.get(url,params=data)
print(res.json())