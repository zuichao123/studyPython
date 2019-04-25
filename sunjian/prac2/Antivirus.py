#coding:utf-8
"""
    目录操作：
        需要导入os模块
        重用函数：
            mkdir(path)创建目录
            makedirs(name)创建目录群
            rmdir(path)删除目录
            removedirs(path)删除目录群
            listdir(path)列出目录中的文件列表
            getcwd()获取当前路径
            chdir(path)更改目录
            walk(top,topdown=True,pnerror=None)

            os.path.basename(path)根据全路径获取文件名称的方法
            os.path.dirname(path)获取文件所在路径的方法
"""
import os
import shutil

print ('#'*20+'欢迎使用sunjian杀毒软件'+"#"*20)

path = input('告诉我你要杀毒的路径（如：C:/Users/Administrator/desktop）')#要杀毒的路径
killContents = input('告诉我你要kill掉的内容（如：abc）')
input('警告：这是删除操作，请客观慎重三思而后行啊...')

print ('正在愉快的帮您删除包含-->'+killContents+'<--的文件和文件夹...')
#（利用os模块中的walk函数实现）返回路径下所有的目录中的文件列表
def dirList2(path):
    try:
        allfile = []#定义一个列表存放所有的文件或目录的绝对路径
        try:
            for path,dir,filelist in os.walk(path):#利用os模块中的wall函数遍历
                for filename in filelist:#再遍历返回的文件列表
                    allfile.append(os.path.join(path,filename))#将路径和文件组合为绝对路径后添加到allfile列表中
            return allfile#返回列表
        except IOError as msg:
            print ('对不起您输入的路径错误...')
            return
    except WindowsError as msg:
        print ('对不起您输入的路径错误...')
        return

#获取当前路径下所有的目录的绝对路径
def getDirPath(path):
    try:
        listDir = []#定义一个放目录路径的列表
        alldf = os.listdir(path)#获取这个路径下的所有的列表
        for df in alldf:#遍历这个列表，
            dfPath = path +'/'+df#获取遍历的目录的绝对路径
            #print dfPath
            if os.path.isdir(dfPath):#判断列表中的元素，是否是目录；如果该路径是目录
                dfs = os.listdir(dfPath)#获取该目录下的所有列表(判断目录中是否有内容)
                if len(dfs)>0:#如果有内容
                    getDirPath(dfPath)#递归判断目录下是否还有目录
                listDir.append(os.path.basename(dfPath))#将该目录的绝对路径添加到列表中
        #print listDir
        return listDir#返回这个放了目录路径的列表
    except WindowsError as msg:
        print ('对不起您输入的路径错误...')
        return

#对文件进行杀毒
def isSrcFile(srcFile):
    try:
        for srcf in srcFile:#遍历该路径下的所有文件
            if open(srcf).name.__contains__(killContents):#如果文件名称包含此关键字
                    print (srcf + ' -->>是文件名中包含了此关键字')
                    os.remove(srcf)#删除之
            else:
                anyfiles = open(srcf).read()#获取文件中的内容
                if anyfiles.__contains__(killContents):#如果文件中的内容包含此关键字
                    print (srcf + ' -->>是文件中的内容包含了此关键字')
                    os.remove(srcf)#删除之
    except WindowsError as msg:
        print ('对不起您输入的路径错误...')
        return
#对目录进行杀毒
def isSrcDir(path):
    try:
        for root, dir, filelist in os.walk(path):  # 遍历当前路径下的所有文件和目录
            for name in dir:#仅遍历所有的目录
                aa = root+'/'+name#获取每一个目录的绝对路径
                if not os.listdir(aa):#如果目录不为空
                    isSrcDir(aa)#递归遍历
                if aa.__contains__(killContents):#如果该目录的名称中包含关键字
                    print (root+'/'+name+'-->>是文件夹的名中包含了此关键字')
                    shutil.rmtree(root+'/'+name)#删除目录之
    except WindowsError as msg:
        print ('对不起您输入的路径错误...')
        return

srcfile = dirList2(path)  # 获取路径下所有的文件的绝对路径
srcdir = getDirPath(path)  # 获取路径下的所有目录的绝对路径的列表

# 执行杀毒 1
isSrcFile(srcfile)
# 执行杀毒 2
isSrcDir(path)
print ('')
# 对该路径下的所有文件进行杀毒:):):)
# print '遍历的文件-->>>'
# print srcfile
#对该路径下的所有目录进行杀毒:):):)
# try:
# print '遍历的目录-->>>'
# for s in srcdir:
#     print path +'/'+ s
# except TypeError,msg:
#     print '对不起您输入的路径错误...'