#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 5:23 下午
#@Author : 钱俊慧
#@File : Xlwt.py
#@Software : PyCharm

import xlwt

# 创建workbook对象
workbook = xlwt.Workbook(encoding='utf-8')
# 创建worksheet工作表
worksheet = workbook.add_sheet('sheet1')
# 写入数据
for i in range(9):
    for j in range(0,i+1):
        worksheet.write(i,j,'%d * %d = %d' % (j+1,i+1,(i+1)*(j+1)))
# 保存
workbook.save('demo.xls')