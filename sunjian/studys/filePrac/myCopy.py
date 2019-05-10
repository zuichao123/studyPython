# -*- coding:utf-8 -*-
'''

'''
import os
import shutil

source_path = os.path.abspath(r'C:\Users\sunjian\Desktop\Zbpl')
target_path = os.path.abspath(r'C:\Users\sunjian\Desktop\Zbpl-附件')

def copyFile(source_path,target_path):
    if not os.path.exists(target_path): # 如果目的文件夹不存在
        os.makedirs(target_path) # 创建
    else:
        shutil.rmtree(target_path)
        os.makedirs(target_path)

    if os.path.exists(source_path): # 如果源文件夹存在
        for root,dirs,files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root,file) # 源文件夹下的文件
                shutil.copy(src_file,target_path) # copy
        print('wancheng...')


copyFile(source_path,target_path)