#-*- codeing = utf-8 -*-
#@Time : 2020/5/21 9:35 上午
#@Author : 钱俊慧
#@File : Sqlite.py
#@Software : PyCharm

# 数据库
import sqlite3


# 1.连接数据库
# conn = sqlite3.connect('Test.db') # 打开或创建数据库文件
# print('Opened database successful!')



# 2.创建数据表
# conn = sqlite3.connect('Test.db') # 打开或创建数据库文件
# c = conn.cursor() # 获取游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real
#         );
# '''
#
# c.execute(sql) # 执行sql语句
# conn.commit() # 提交数据库操作
# conn.close() # 关闭数据库连接
#
# print('成功建表！')



# 3.插入数据
# conn = sqlite3.connect('Test.db') # 打开或创建数据库文件
# c = conn.cursor() # 获取游标
#
# sql1 = '''
#     insert into company(id, name, age, address, salary)
#      values (1, 'qq', 17, '安徽', 8000);
# '''
#
# sql2 = '''
#     insert into company(id, name, age, address, salary)
#      values (2, 'QQ', 27, '北京', 15000);
# '''
#
# c.execute(sql1) # 执行sql语句
# c.execute(sql2) # 执行sql语句
# conn.commit() # 提交数据库操作
# conn.close() # 关闭数据库连接
#
# print('插入数据成功！')



#  4.查询数据
conn = sqlite3.connect('Test.db') # 打开或创建数据库文件
c = conn.cursor() # 获取游标

sql = 'select id,name,age,address,salary from company'

cursor = c.execute(sql) # 执行sql语句
for row in cursor:
    print(row)
    print('id = ',row[0],'\n')

conn.close() # 关闭数据库连接

print('查询数据成功！')


