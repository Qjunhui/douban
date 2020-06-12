#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 9:39 上午
#@Author : 钱俊慧
#@File : test.py
#@Software : PyCharm

import urllib.request

# 1.获取一个get请求
# response = test.request.urlopen('http://www.baidu.com')
# html = response.read().decode('utf-8')
# print(html)



# 2.获取一个post请求
# 模拟用户登陆
import urllib.parse
# data = bytes(test.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response = test.request.urlopen('http://httpbin.org/post',data=data)
# html = response.read().decode('utf-8')
# print(html)



# 3.超时处理
# try:
#     response = test.request.urlopen('http://httpbin.org/get',timeout=0.01)
#     html = response.read().decode('utf-8')
#     print(html)
# except test.error.URLError:
#     print('time out!')



# 4.response.status
# response = test.request.urlopen('http://douban.com')
# print(response.status) # 418 发现是个爬虫



# 5
# response = test.request.urlopen('http://baidu.com')
# print(response.getheaders())
# print(response.getheader('Server'))



# 6.爬虫
# url = 'http://httpbin.org/post'
# data = bytes(test.parse.urlencode({'hello':'world'}),encoding='utf-8')
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
# }
# req = test.request.Request(url=url,data=data,headers=headers,method='POST')
# response = test.request.urlopen(req)
# html = response.read().decode('utf-8')
# print(html)



# 7.豆瓣
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.douban.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
req = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
print(html)