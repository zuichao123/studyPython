from fabric.api import *

env.hosts = ['192.168.195.129']
env.user = 'sunjian'
env.password = '123456'

@runs_once
@task
def local_update():
    with lcd("/home/sunjian/github/studyPython"):
    	local("git add -A")
	local("git commit -m 'update le yi dian'")
	local("git pull origin master")
	local("git push origin master")

@task
def remote_update():
    with cd("/home/sunjian/github/studyPython"):
	#run("git checkout master")
	run("git pull origin master")

@task
def deploy():
    local_update()
    remote_update()
	


