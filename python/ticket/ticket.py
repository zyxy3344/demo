__author__ = "紫羽"

import config

import requests
import random
import json
# cookie 保持
session = requests.Session()
hearders = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
session.headers.update(hearders)
# 获取登录页面
login_page_url = 'https://kyfw.12306.cn/otn/login/init'
session.get(login_page_url)
print(session.cookies)
# 下载验证码
captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&0.6958119199757788'
# requests 请求参数的构建
data = {
    'login_site': 'E',
    'module': 'login',
    'rand': 'sjrand',
    str(random.random()):'',
}
captcha_response = session.post(captcha_url, data=data)
with open('capcha.jpg', 'wb')as f:
    f.write(captcha_response.content)

# 校验验证码
point = {
    '1':'35,43',
    '2':'108,403',
    '3':'185,43',
    '4':'254,43',
    '5':'34,117',
    '6':'108,117',
    '7':'180,117',
    '8':'258,117',
}
def get_point(nums):
    nums = nums.split(',')
    temp = []
    for item in nums:
        temp.append(point[item])
    return ','.join(temp)
check_captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check'
# 构建请求参数
captcha_data = {
    'answer': get_point(input('请输入正确的坐标>>:')),
    'login_site': 'E',
    'rand': 'sjrand'
}
check_response = session.post(check_captcha_url, data=captcha_data)
print(check_response)
check_res = check_response.json()
print(check_res)
if check_res['result_code'] != '4':
    exit('验证码校验失败!')

# 校验用户名和密码
login_url = 'https://kyfw.12306.cn/passport/web/login'
login_data = {
    'username': config.username,
    'password': config.password,
    'appid': 'otn'
}
login_response = session.post(login_url, data=login_data)
# login_res = login_response.json()
# print(login_res)
if login_response.json()['result_code'] != 0:
    exit('用户名密码错误')


# 获取权限token
uamtk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
uamtk_data = {
    'appid': 'otn'
}
uamtk_response =session.post(uamtk_url, data=uamtk_data)
print(uamtk_response.json())

# 获取权限
auth_url = 'https://kyfw.12306.cn/otn/uamauthclient'
auth_data = {
    'tk':uamtk_response.json()['newapptk']
}
res = session.post(auth_url, data=auth_data)
print(res.text)

# import requests
# import json
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# class Ticket:
#     url = 'https://kyfw.12306.cn/otn/leftTicket/init'
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#         'Cookie': '_T_WM=ded9008adaa017fdf8eb124854945f13; ALF=1532330775; SCF=ApU2_HATFQCAT10qPsaQc4KkqFFOZNsrR_IaKYXUzIuAdoscs91d2eHbIEoY-diTdoCo4BWF0HNJ1Unf5OCye_k.; SUB=_2A252KYZIDeRhGeNN61MX9SrPzDyIHXVV1SoArDV6PUNbktANLU7hkW1NSfUqaKEjLg7SghWEa9uY5luGIfGnQnWt; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWzOpH3I95fGAawDbJDTcdx5JpX5KMhUgL.Fo-0eh2cSKB0S052dJLoIp7LxKnLBK2L1h5LxKnLB.-LBo5fe05pSo-Xe0M7; SUHB=079TBKtaRmzorT; SSOLoginState=1529738776'
#     }
#     data = {
#         'leftTicketDTO.train_date': '2018 - 07 - 31',
#         'leftTicketDTO.from_station': 'YIJ',
#         'leftTicketDTO.to_station': 'WUJ',
#         'purpose_codes': '0X00'
#     }
#
#     def load_html(self):
#         html = requests.post(self.url, data=self.data, headers=self.headers).content.decode('utf-8')
#         print(html)
#
# def main():
#     S = Ticket()
#     S.load_html()
#
# if __name__ == '__main__':
#     # main()
#     url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-31&leftTicketDTO.from_station=YIJ&leftTicketDTO.to_station=WUJ&purpose_codes=0X00'
#
#     html = requests.get(url).text
#     import json
#     j = json.loads(html)['data']['result'][0].split('|')[4]
#
#
#     url1 = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
#     html1 = requests.get(url1).text.replace(r"var station_names =",'')
#     print(html1)