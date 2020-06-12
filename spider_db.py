#-*- codeing = utf-8 -*-
#@Time : 2020/5/21 1:43 下午
#@Author : 钱俊慧
#@File : spider_db.py
#@Software : PyCharm


from bs4 import BeautifulSoup
import re
import urllib.request
import urllib.error
import sqlite3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import xlwt


def main():
    baseUrl = "https://movie.douban.com/top250?start="
    #1.爬取网页
    dataList = getData(baseUrl)
    dbPath = "douban.db"
    #3.保存数据
    saveDataDB(dataList,dbPath)

# 影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片的规则
findImgSrc = re.compile(r'<img .*src="(.*?)"',re.S)
# 影片片名的规则
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片评分的规则
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价人数的规则
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 概况的规则
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关内容的规则
findBD = re.compile(r'<p class="">(.*?)</p>',re.S)


#爬取网页
def getData(baseUrl):
    dataList = []
    for i in range(0,10): # 每页25条数据，共10页
        url = baseUrl + str(i*25)
        html = askURL(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html,'html.parser')
        for item in soup.find_all('div',class_='item'):
            data = []
            item = str(item)

            link = re.findall(findLink,item)[0] # 影片详情链接
            data.append(link)

            imgSrc = re.findall(findImgSrc,item)[0] # 影片图片
            data.append(imgSrc)

            titles = re.findall(findTitle, item)  # 影片片名
            if(len(titles) == 2):
                ctitle = titles[0]  # 中文名
                data.append(ctitle)
                otitle = titles[1].replace('/','') # 外国名
                data.append(otitle)
            else:
                data.append(titles[0])
                data.append(' ') # 外国名为空，避免后续数据错位

            rating = re.findall(findRating, item)[0]  # 影片评分
            data.append(rating)

            judge = re.findall(findJudge, item)[0]  # 影片评价人数
            data.append(judge)

            inq = re.findall(findInq, item)  # 影片概况
            if len(inq) != 0:
                inq = inq[0].replace('。', '')
                data.append(inq)
            else:
                data.append(' ')

            bd = re.findall(findBD, item)[0]  # 影片相关内容
            bd = re.sub('<br(\s+)?\/?>(\s+)?',' ',bd) # \s表示空白字符
            bd = re.sub('/', ' ', bd)
            data.append(bd.strip())

            dataList.append(data)
    return dataList

# 得到指定url的网页内容
def askURL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    request = urllib.request.Request(url, headers=headers)
    html = ''
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return html


#保存数据
def saveDataDB(dataList,dbPath):
    # init_db(dbPath)
    conn = sqlite3.connect(dbPath) # 打开或创建数据库文件
    c = conn.cursor() # 获取游标

    # 插入数据
    for data in dataList:
        print(data)
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"' + data[index] + '"'
        sql = '''
            insert into movie250(info_link, imgSrc_link, ctitle, otitle, rating, judge, inq, bd)
             values (%s);
        ''' % ",".join(data)

        c.execute(sql)  # 执行sql语句
        conn.commit() # 提交数据库操作

    c.close()
    conn.close() # 关闭数据库连接


# 创建数据表
def init_db(dbPath):
    sql = '''
        create table movie250(
            id integer primary key autoincrement,
            info_link text,
            imgSrc_link text,
            ctitle varchar,
            otitle varchar,
            rating numeric,
            judge numeric,
            inq text,
            bd text
        )
    '''
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    c.execute(sql)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()