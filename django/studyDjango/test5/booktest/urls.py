from django.conf.urls import re_path
from . import views

urlpatterns=[
    # 静态文件
    re_path(r'^$', views.index),
    # 中间件
    re_path(r'^myException$', views.myException),
    # 上传文件
    re_path(r'^uploadPic$', views.uploadPic),
    re_path(r'^uploadHandle$', views.uploadHandle),
    # 分页
    re_path(r'^herolist/(\d*)$', views.herolist), # 将数字传递给视图函数
    # 下拉选择
    re_path(r'^index$', views.index),
    re_path(r'^pro$', views.pro),
    re_path(r'^city(\d+)/$', views.city),
    re_path(r'^area(\d+)/$', views.area),
    # 富文本编辑器
    re_path(r'^htmlEditor$', views.htmlEditor),
    re_path(r'^htmlEditorHandle', views.htmlEditorHandle),
    # 缓存
    re_path(r'^cache1$', views.cache1),
]
