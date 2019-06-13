# coding:utf-8

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from django.views.decorators.cache import cache_page

from .models import *

# 静态文件
def index(request):
    return render(request, 'booktest/index.html')

# 中间件
def myException(request):
    return HttpResponse('hello exception')

# 上传文件
def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')
def uploadHandle(request):
    pic1 = request.FILES['pic1'] # 接收
    picName = os.path.join(settings.MEDIA_ROOT, pic1.name) # 存储到服务器的路径下
    with open(picName, 'wb') as pic: # 读取文件内容
        for c in pic1.chunks(): # 循环写
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s"/>'%pic1.name) # 输出到浏览器

# 进行分页练习
def herolist(request,pindex):
    if pindex == '':
        pindex = '1'
    list = HeroInfo.objects.all() # 获取所以英雄数据
    print("--------------------",pindex)
    paginator = Paginator(list,10) # 进行分页
    page = paginator.page(int(pindex)) # 获取页的对象
    context = {'page':page}
    return render(request, 'booktest/herolist.html', context)

# 省市区选择
def index(request):
    return render(request, 'booktest/area.html')
# 省
def pro(request):
    data = Province.objects.all() # 查询所有数据
    list = []
    for area in data: # 遍历查询到的所有列表元素
        list.append([area.provinceID, area.province]) # 将查询到的id/title字段添加到list列表中
    return JsonResponse({'data':list}) # 将这个列表转成json格式后返回
# 市
def city(request,id):
    print('city')
    cityList = City.objects.filter(father=id)
    list = []
    for item in cityList:
        list.append({'id':item.cityID, 'city':item.city})
    return JsonResponse({'data':list})
# 区
def area(request, id):
    print('area')
    areaList = Area.objects.filter(father=id)
    list = []
    for item in areaList:
        list.append({'id':item.areaID, 'area':item.area})
    return JsonResponse({'data':list})

# 自定义富文本编辑器
def htmlEditor(request):
    return render(request, 'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html = request.POST['hcontent']
    test1 = Test1.objects.get(pk=1)
    test1.content = html
    test1.save()
    context = {'context':html}
    return render(request, 'booktest/htmlShow.html', context)

# 缓存
@cache_page(60*10)
def cache1(request):
    return HttpResponse('hello1')

# 全文搜索+中文分词
def mysearch(request):
    return render(request, 'booktest/mysearch.html')