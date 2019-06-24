from fabric.api import *

env.hosts=['127.0.0.1']
#env.password='python'
env.passwords = {
    'sunjian@127.0.0.1:22':'123456'
}

@runs_once
def input_raw():
    return prompt("please input directory name:", default="/home")

def workask(dirname):
    run('ls -l ' + dirname)

@task
def go():
    print('start ...')
    getdirname = input_raw()
    workask(getdirname)
    print('end ...')
