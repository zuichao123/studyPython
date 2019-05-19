#coding:utf-8
#打开文件，读取内容
"""
    r   只读
    r+  读写
    w   写入，先删除源文件，再重新写入，如果没有文件就创建
    w+  读写，先删除原文件，在重新写入，如果没有文件就创建
    a   写入，在文件末尾追加新的内容，文件不存在，创建之
    a+  读写，在文件末尾追加新的内容，文件不存在，创建之
    b   打开二进制的文件。可以与r,w,a,+结合使用
    U   支持所有的换行符号，\r \n \r\n
"""
url = 'C:/Users/sunjian/desktop/a.txt'
url2 = 'C:/Users/sunjian/desktop/b.txt'
url3 = 'C:/Users/sunjian/desktop/c.txt'
url4 = 'C:/Users/sunjian/desktop/d.txt'
url5 = 'C:/Users/sunjian/desktop/e.txt'

fo = open(url,'r')#打开文件,只读模式
print (fo.read())#读取输出
fo.close()#关闭

#向文件中写入内容(w 清空源文件，重新写入；w+)
fnew = open(url2,'a+')#读写模式，追加内容模式
fnew.write('hello \n woshi sunjian')#此时还在缓存中
fnew.close()#写入文件中
fnew = open(url2)#再次打开
print (fnew.read())#读取输出
fnew.close()#关闭

"""
    readLine  每次读取文件的一行（size是指每行每次读取的size个字节直到行的末尾）
    readLines 读取所有行，返回一个列表（一行为一个元素）;可以使用next()进行遍历,但是一次取一行，取到空时，提示：StopIteration
"""
#readLine
f1 = open(url2)#打开文件
print (f1.readline())#读取一行
f1.close()#关闭
#readLines
f2 = open(url2)#打开文件
print ('url2-->',f2.readlines())#读取所有行
#print f2.next()#遍历输出一行
f2.close()#关闭

"""
    write       一次写一个字符串；在写入前是否会清空原来的数据，取决于打开时的模式
    writelines  多行写入；在写入前是否会清空原来的数据，取决于打开时的模式
    seek        传入参数为0：文件指针指向文件头部；
                传入参数为1：文件指针指向文件当前位置；
                传入参数为2：文件指针指向文件尾部；
    flush       提交更新文件
"""
#writelines
l = ['one\n','two\n','three\n']
ff1 = open(url3,'a')#写入模式打开文件url3，可追加内容
ff1.writelines(l)#写入在缓存中
ff1.close()#写入
ff1 = open(url3,'r')#只读模式打开文件
print ('url3-->',ff1.readlines())#读取输出内容
ff1.close()#关闭文件

#seek
ff2 = open(url4,'a+')#打开url4文件
ff2.writelines(l)#将列表l写入文件中，此时还在内存中
ff2.close()#写入文件中
ff2 = open(url4,'r+')#再次打开
ff2.seek(0,2)#移动指针到文件的结尾，此时不能读取到内容
print ('seek-->',ff2.read())#读取
ff2.close()#关闭文件

#flush
ff3 = open(url5,'w+')
ff3.writelines(l)
ff3.flush()
print ('url5-->',ff3.readlines())#此时已经写入了
ff3.close()

"""
    小例子：
        查找一个文件中有多少个hello字符串
"""
import re
fp = open(url3,'r')#只读模式打开文件
count = 0
for s in fp.readlines():
    li = re.findall('hello',s)
    if len(li) > 0:
        count = count+len(li)

print ('此文件中共有',count,'个hello')
fp.close()

"""
    小例子：
        1.把以上文件中的hello替换成China，保存到a2.txt中
        2.把例子1文件中的hello替换成python
"""
#先把url3中的内容存储到url6中
url6 = 'C:/Users/sunjian/desktop/6.txt'
url7 = 'C:/Users/sunjian/desktop/7.txt'
u3 = open(url3,'a+')#可读可写在文件后追加的方式打开url3文件
uu3 = u3.readlines()#读取文件的内容赋值到uu3
u3.close()#关闭url3文件
u6 = open(url6,'w')#打开url6文件，可写删除原文件重新写入模式
u6.writelines(uu3)#将uu3中的内容写入到url6文件中，此时还在内存中
u6.close()#关闭文件==存储到文件中
u6 = open(url6,'r')#打开url6文件
print ('url6-->',u6.readlines())#读取输出内容
u6.close()#关闭文件

#######例子 1（将url6中的hello 替换成China存储到url7文件中）
fp1 = open(url6,'r')#读取第一个文件
fp2 = open(url7,'w')#写入到第二个文件（删除源文件，重新写入模式）
for s in fp1.readlines():#遍历url6中的内容
    fp2.write(s.replace('hello','china'))#将遍历到的内容中的hello替换成China后写入到url7文件中
fp1.close()#关闭url6文件
fp2.close()#关闭url7文件

fp2 = open(url7,'r')#重新打开url7文件
print ('url7-->',fp2.readlines())#读取输出文件内容
fp2.close()#关闭文件

#########例子 2（将url3文件中的内容存储到url8文件中，并将url8文件中的hello替换成Python）
url8 = 'C:/Users/sunjian/desktop/8.txt'
u3 = open(url3,'a+')#打开url3文件，可读写，可追加模式
uu3 = u3.readlines()#读取内容存储到uu3变量中
u3.close()#关闭url3文件
u8 = open(url8,'w')#只写模式，删除原文件，打开url8文件
u8.writelines(uu3)#将变量uu3中内容写入到url8文件中
u8.close()#关闭url8文件
u8 = open(url8,'r')#重新打开url8文件
print ('url8-->',u8.readlines())#读取输出文件内容
#开始替换
fp3 = open(url8,'r+')#可读写模式模式打开url8文件
s = fp3.read()#读取文件内容到变量s中3
fp3.seek(0,0)#将角标重新移动到文件开始位置
fp3.write(s.replace('hello','python'))#将读取到的内容中的hello替换成phthon后，重新写入到文件中
fp3.close()#关闭存储文件内容
fp3 = open(url8,'r')#重新打开url8文件
print ('url8-->',fp3.readlines())#读取输出文件内容
fp3.close()#关闭文件