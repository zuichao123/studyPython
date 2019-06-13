from django.shortcuts import render

# Create your views here.
from .models import BookInfo
from django.db.models import Max, F, Q


def index(request):
    # bookList = BookInfo.books1.filter(id__in=[1,2])
    # bookList = BookInfo.books1.filter(pk__gt=3) # id小于3的  gt是大于
    # bookList = BookInfo.books1.aggregate(Max('bpub_date'))
    # bookList = BookInfo.books1.filter(bread__gte=F('bcommet'))
    bookList = BookInfo.books1.filter(pk__lt=6,btitle__contains='天') # 逻辑与--主键小于6，并且名字中包含天的
    # bookList = BookInfo.books1.filter(Q(pk__lt=6)| Q(btitle__contains='天')) # 逻辑或--主键小于6，或名字中包含天的

    context = {'list':bookList}
    return render(request, 'booktest/index.html', context)