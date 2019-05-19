#coding：utf-8
'''
    functools简谈
'''
import functools

# --------------------------partial
def showarg(*args, **kwargs):
    print(args)
    print(kwargs)

# 调用partial方法时的参数1,2,3默认传递给showarg函数
p1 = functools.partial(showarg,1,2,3)

print(p1())
print(p1(4,5,6))
print(p1(a='python', b='sunjian'))

p2 = functools.partial(showarg,a = 3, b='windows')
print(p2())
print(p2(2,3))
print(p2(a='python',b='jack'))

# ------------------------------wraps
def note(func):
    'note function'
    @functools.wraps(func) # 添加上这个之后，下边test()函数的装饰就失效了，就不会运行note函数中的闭包了
    def warpper():
        'wrapper function'
        print('note something')
        return func()
    return warpper

@note
def test():
    'test function'
    print('i am tester')

test()
print(test.__doc__)