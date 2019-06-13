from django.conf.urls import url,re_path
from .import views



urlpatterns=[
    re_path(r'^$', views.index, name='index'),
    re_path(r'^(\d+)$', views.show, name='show'),

    re_path(r'^index2', views.index2, name='index2'),
    re_path(r'^user1', views.urer1, name='user1'),
    re_path(r'^user2', views.urer2, name='user2'),
    re_path(r'^htmlTest', views.htmlTest, name='htmlTest'),

    re_path(r'^csrf1', views.csrf1, name='csrf1'),
    re_path(r'^csrf2', views.csrf2, name='csrf2'),

    re_path(r'^verifyCode', views.verifyCode, name='verifyCode'),
    re_path(r'^verifyTest1', views.verifyTest1, name='verifyTest1'),
    re_path(r'^verifyTest2', views.verifyTest2, name='verifyTest2'),
]
