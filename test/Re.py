#-*- codeing = utf-8 -*-
#@Time : 2020/5/20 3:06 下午
#@Author : 钱俊慧
#@File : Re.py
#@Software : PyCharm


import re

# 1)re.search()
# pat = re.compile('AA')  # AA是规则
# m = pat.search('CSAA')  # CSAA是被校验的内容

# m = re.search('AA','CSAA')


# 2)re.match()


# 3)re.findall()
# m = re.findall('[A-Z]','qdQDWas')


# 4)re.split()

# 5)re.finditer()

# 6)re.sub()
# m = re.sub('a','A','asdfwefqa')


m = r"\aasd\'"
print(m)