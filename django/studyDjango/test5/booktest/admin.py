from django.contrib import admin
"""
    站点管理，在admin账号中添加
"""
# 添加管理app
from .models import *

# 定义一个模板类
# @admin.register(HeroInfo) # 这个表示在HeroInfo这个APP下也注册这个自定义的模板，用一下方式显示（与admin.site.register(HeroInfo, BookInfoAdmin)的方式一样）
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date'] # 界面中显示的列
    pass

# 给BookInfo这个APP注册一个自定义模板
admin.site.register(BookInfo, BookInfoAdmin)

# 注册Test1类到admin
admin.site.register(Test1)

