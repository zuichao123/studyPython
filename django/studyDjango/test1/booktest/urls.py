from django.urls import path, re_path
from . import views

urlpatterns=[
    path(r'book/',views.index),
    re_path(r'book/(\d+)',views.show)
]