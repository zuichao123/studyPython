#coding:utf-8
'''
    常用模块
'''
# ---------------------加密
import hashlib
import datetime
KEY_VALUE = 'sunjian123'
now = datetime.datetime.now()
str = '%s%s' % (KEY_VALUE,now.strftime('%Y%m%d'))

m = hashlib.md5()
m.update(str.encode('utf-8'))
value = m.hexdigest()

print(value)

# 其他模块需要用到时再研究