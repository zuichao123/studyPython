from django.conf.urls import re_path,url
from .import views

urlpatterns = [
    re_path(r'^register/$', views.register),
    re_path(r'^register_handle/$', views.register_handle),
]