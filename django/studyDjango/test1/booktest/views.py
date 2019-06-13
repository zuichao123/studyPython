from django.shortcuts import render

# Create your views here.
from .models import BookInfo


def index(request):
    # temp = loader.get_template('booktest/index.html')
    # return HttpResponse(temp.render())
    bookList = BookInfo.objects.all() # 执行查找所有的书籍的语句
    context = {'list':bookList}
    return render(request, 'booktest/index.html', context)

def show(request,id):
    book = BookInfo.objects.get(pk=id) # 根据id查找书，返回此书的对象
    heroList = book.heroinfo_set.all() # heroinfo_set表示关联的对象；all()表示查询
    context = {'list':heroList}

    print(len(heroList))
    return render(request, 'booktest/bookShow.html', context)