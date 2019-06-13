from django.contrib import admin

# Register your models here.
from booktest.models import HeroInfo, BookInfo


class HeroInfoInline(admin.StackedInline): # 列表的形式 # admin.TabularInline(表格的形式)
    """关联添加类"""
    model = HeroInfo # 关联的类名
    extra = 2 # 关联的条数

class BookInfoAdmin(admin.ModelAdmin):
    """自定义显示类"""
    list_display = ['id','btitle','bpub_date'] # 显示字段，可以点击列头排序
    list_filter = ['btitle'] # 过滤字段，过滤框出现在右侧
    search_fields = ['btitle'] # 搜索字段
    list_per_page = 10 # 分页

    fieldsets = [ # 编辑时的分组
        ('base',{'fields':['btitle']}), # base组显示的字段
        ('super',{'fields':['bpub_date']}) # super组显示的字段
    ]

    inlines = [HeroInfoInline] # 关联上

# Register your models here.
admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo)