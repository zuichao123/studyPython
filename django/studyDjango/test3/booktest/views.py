from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse(request.path)

def detail(request, p1):
    return HttpResponse(p1)

# 展示链接的页面
def getTest1(request):
    return render(request,'booktest/getTest1.html')

# 接收一键一值的情况
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    context = {'a':a1,'b':b1,'c':c1}
    return render(request,'booktest/getTest2.html', context)

# 接收一键多值的情况
def getTest3(request):
    a = request.GET.getlist('a')
    context = {'a':a}
    return render(request,'booktest/getTest3.html',context)

def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST.get('ugender')
    uhobby = request.POST.getlist('uhobby')
    context = {'uname':uname,'upwd':upwd,'ugender':ugender,'uhobby':uhobby}

    return render(request, 'booktest/postTest2.html', context)

# cookie练习
def cookieTest(request):
    response = HttpResponse()
    if request.COOKIES.has_key('t1'):
        response.write(request.COOKIES['t1'])
    response.set_cookie('t1','abcdefg')

    return response


# 重定向练习
def redTest1(request):
    return HttpResponseRedirect('/booktest/redTest2/')

def redTest2(request):
    return HttpResponse('这是重定向过来的')


# session练习
def session1(request):
    uname = request.session.get('myname','未登录')
    context = {'uname':uname}
    return render(request, 'booktest/session1.html',context)

def session2(request):
    return render(request,'booktest/session2.html')

def session3(request):
    uname = request.POST['uname']
    request.session['myname']=uname
    request.session.set_expiry(0) # 设置session在浏览器关闭时过期
    return redirect('/booktest/session1/')

def session4(request):
    # 删除session
    del request.session['myname']
    return redirect('/booktest/session1')