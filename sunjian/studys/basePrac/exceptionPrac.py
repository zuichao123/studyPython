#coding:utf-8
"""
    :raise抛出异常
"""
filename = input('请输入要操作的文件：')
try:
    f = open(filename)
    print ('hello')
except IOError as msg:#自定义异常
    print ('你指定的文件不存在')
finally:
    try:
        f.close()
    except NameError as msg:
        pass

if filename == 'hello':
    raise TypeError('nothing!!!!')