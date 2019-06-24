from fabric.api import *

env.user = 'sunjian'
env.hosts = ['127.0.0.1','192.168.195.129']
env.password = '123456'

@task
@runs_once
def tar_task():
    with lcd('/home/sunjian/Desktop'):
	local('tar zcvf 999.tar.gz 999.py')
	local('rm -rf 999.py')

@task
def put_task():
    run('mkdir -p /home/sunjian/sunjian')
    with cd('/home/sunjian/Desktop'):
	put('/home/sunjian/Desktop/999.tar.gz', '/home/sunjian/sunjian/999.tar.gz')

@task
def check_task():
    lmd5 = local('md5sum /home/sunjian/Desktop/999.tar.gz', capture=True).split(' ')[0]
    rmd5 = run('md5sum /home/sunjian/sunjian/999.tar.gz').split(' ')[0]
    if lmd5 == rmd5:
	print('OK ...')
    else:
	print('error...')

@task
def run_task():
    with cd('/home/sunjian/sunjian'):
	run('tar zxvf 999.tar.gz')
	run('python 999.py')

@task
def go():
    tar_task()
    put_task()
    check_task()
    run_task()
