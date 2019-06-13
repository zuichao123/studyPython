from django.conf.urls import url,re_path
from .import views



urlpatterns=[
    re_path(r'^$', views.index),
    re_path(r'^(\d+)$', views.detail), # 获取url中的数字作为参数传递给detail视图函数

    re_path(r'^getTest1/$', views.getTest1),
    re_path(r'^getTest2/$', views.getTest2),
    re_path(r'^getTest3/$', views.getTest3),

    re_path(r'^postTest1/$', views.postTest1),
    re_path(r'^postTest2/$', views.postTest2),

    re_path(r'^cookieTest/$', views.cookieTest),

    re_path(r'^redTest1/$', views.redTest1),
    re_path(r'^redTest2/$', views.redTest2),

    re_path(r'^session1/$', views.session1),
    re_path(r'^session2/$', views.session2),
    re_path(r'^session3/$', views.session3),
    re_path(r'^session4/$', views.session4),

]
