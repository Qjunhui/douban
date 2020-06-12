#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 1:18 下午
#@Author : 钱俊慧
#@File : Bs4.py
#@Software : PyCharm

# ⚠️注意：文件名不能命名为bs4.py,会报错：cannot import name 'BeautifulSoup' from partially initialized module 'bs4'
# 【如果命名成了bs4.py,程序则会在该文件下去找beautifulsoup，所以会报错】

from bs4 import BeautifulSoup

file = open('./baidu.html','rb')
html = file.read().decode('utf-8')
bs = BeautifulSoup(html,'html.parser')


# 1.Tag 标签及其内容：只能拿到所找到的第一个内容
# print(bs.title)
# print(bs.a)
# print(bs.head)
# print(type(bs.head))


# 2.NavigableString 标签里的内容
# print(bs.title.string)
# print(type(bs.title.string))
# print(bs.a.attrs) # 获取a标签的所有属性


# 3.BeautifulSoup 表示整个文档
# print(type(bs))
# print(bs.name) # [document]
# print(bs.attrs) # {}


# 4.Comment 特殊的NavigableString，输出内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))



#-----------------------------------------------------------------------

# 1.文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])


# 2.文档的搜索
# 1）find_all():字符串过滤
# t_list = bs.find_all('a')

import re
# search():正则表达式
# t_list = bs.find_all(re.compile('a'))

# 方法；传入一个函数（方法），根据函数的要求来搜索
# def name_is_exist(tag):
#     return tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exist)


# 2)kwargs 参数
# t_list =  bs.find_all(id="head")
# t_list =  bs.find_all(class_=True)


# 3)text参数
# t_list =  bs.find_all(text = "视频")
# t_list =  bs.find_all(text = ["视频","贴吧"])
# t_list =  bs.find_all(text = re.compile('\d'))


# 4)limit 参数
# t_list =  bs.find_all('a',limit=3)



# css选择器
# t_list = bs.select('a')
# t_list = bs.select('.mnav')
# t_list = bs.select('#head')
# t_list = bs.select('a[href="http://news.baidu.com"]')
t_list = bs.select('head>title')

for item in t_list:
    print(item)