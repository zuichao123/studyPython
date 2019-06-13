# coding:utf-8
from _sha1 import sha1
from django.shortcuts import render, redirect

from .models import UserInfo


def register(request):
    return render(request, 'df_user/register.html')

def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    upwd2 = post.get('cpwd')
    uemail = post.get('email')
    # 判断两次密码
    if upwd != upwd2:
        return redirect('/user/register')
    # 密码加密
    s1 = sha1()
    s1.update(upwd.encode("utf-8"))
    upwd3 = s1.hexdigest()
    # 创建对象
    user = UserInfo()
    user.uname = uname
    user.upwd = upwd3
    user.uemail = uemail
    user.save()
    # 注册成功，转到登录界面
    return redirect('/user/login/')
