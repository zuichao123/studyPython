#coding:utf-8
"""
    python 基础语法练习
"""
def f(x,*args,**args2):
    print ("x=" "%s" % x)
    print ("args=",args)
    print ("args2=",args2)

t=(2,3,5,6)
tt={'a':3,'b':4,'c':5}
f(*t,**tt)
print "****************"
def ff(x,y):
    return x*y
print ff(3,3)

v=lambda x,y:x*y
print v(4,5)
print "lambda************"
l = range(1,33)
print l
print reduce(lambda x,y:x*y, l)
print "***************"
print abs(-10)
print divmod(3,7)
print pow(3,4)
print round(3)
print callable(f)
tttt=[3,5,6,4]
print type(t)
print cmp(6,5)
print range(1,10)
print xrange(1,10)
print tuple(tttt)
# help(ord)
print ord('k')
#oct chr ord
s='hello world'
print s.capitalize()
print s.replace('hello','good')
print s.replace('o','x',1)
print s.split(" ")
print "****************************"
l=range(10)
print l
def f(x):
    if x%2==0:
        return x
ll= filter(f,l)
print ll
print zip(l,ll)
print map(None,l,ll)
j=[1,3,5]
jj=[2,4,6]
def mf(x,y):
    return x*y
print map(mf,j,jj)
print "*********************"
l=range(1,101)
def rf(x,y):
    return x+y
print reduce(rf,l)
print reduce(lambda x,y:x+y,l)
print filter(lambda x:x%2 ==0,l)
