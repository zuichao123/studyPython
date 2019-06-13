from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def index(request):
    # hero = HeroInfo.objects.get(pk=1) # 查询主键为1的英雄
    # context = {'hero':hero}

    list = HeroInfo.objects.filter(isDelete=True)
    context = {'list':list}

    return render(request, 'booktest/index.html', context)

def show(request,id):
    context = {'id':id}
    return render(request, 'booktest/show.html', context)

# 模板继承练习
def index2(requet):
    return render(requet, 'booktest/index2.html')

def urer1(request):
    context = {'name':'孙健'} # 传递值到模板中，哪一层接收都可以
    return render(request, 'booktest/user1.html', context)

def urer2(request):
    return render(request, 'booktest/user2.html')

# html转义
def htmlTest(request):
    context = {'t1':'<h1>234</h1>'}
    return render(request, 'booktest/htmlTest.html', context)

# csrf 跨站伪造
def csrf1(request):
    return render(request, 'booktest/csrf1.html')

def csrf2(request):
    uname = request.POST['uname']
    return HttpResponse(uname)

# 验证码pip install pillow
def verifyCode(request):
    # PIL是python2版本的图像处理库，不过现在用Pillow比PIL强大，是python3的处理库
    # 引入绘画模块
    from PIL import Image, ImageDraw, ImageFont
    from django.http import HttpResponse
    # 导入随机数模块
    import random
    from io import BytesIO

    # text = 'ABCD'
    # # 逐个绘制字符
    # textTemps = ''
    # for t1 in text:
    #     textTemp = text[random.randrange(0,len(text))] # 每次生成一个字符
    #     textTemps += textTemp # 拼接到一起
    #     draw.text((t1*25,0),textTemp,(255,255,255),font) # 绘制这个字符
    # # 释放画笔

    # 1，定义变量，用于画面的背景色、宽、高
    # random.randrange(20, 100)意思是在20到100之间随机找一个数
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 0)
    width = 100
    height = 30
    # 2，创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 3，创建画笔对象
    draw = ImageDraw.Draw(im)
    # 4，调用画笔的point()函数绘制噪点，防止攻击
    for i in range(0, 100):
        # 噪点绘制的范围
        xy = (random.randrange(0, width), random.randrange(0, height))
        # 噪点的随机颜色
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        # 绘制出噪点
        draw.point(xy, fill=fill)
    # 5，定义验证码的备选值
    text = 'ABCD123EFGHJK456LMNPQRS789TUVWXYZ0'

    # 6，构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”
    # arial.ttf window下的字体
    font = ImageFont.truetype('arial.ttf', 23)
    # 7，构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))

    # 8，随机绘制4个值作为验证码
    textTemp = ''
    for i in range(4):
        textTemp1 = text[random.randrange(0,len(text))]
        textTemp += textTemp1
        draw.text((i*25,0),textTemp1,fontcolor,font)
    # 将验证码设置到session中
    request.session['code'] = textTemp
    # 9，用完画笔，释放画笔
    del draw
    # 10，内存文件操作
    buf = BytesIO()
    # 11，将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    # 12，将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


def verifyTest1(request):
    return render(request, 'booktest/verifyTest1.html')

def verifyTest2(request):
    code = request.POST['code1'] # 获取文本框中输入的验证码
    code2 = request.session['code'] # 获取生成验证码
    if code == code2:
        return HttpResponse('ok')
    else:
        return HttpResponse('no')
    
