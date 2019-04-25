#coding:utf-8
"""
    :raise抛出异常
"""
filename = raw_input('请输入要操作的文件：')
try:
    f = open(filename)
    print 'hello'
except IOError,msg:
    print '你指定的文件不存在'
finally:
    try:
        f.close()
    except NameError,msg:
        pass

if filename == 'hello':
    raise TypeError('nothing!!!!')