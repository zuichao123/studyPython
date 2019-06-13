from django.db import models

"""
    对于数据的操作类
"""

class BookInfoManager(models.Manager):
    """资源管理器类--是模型类的属性，用于将对象与数据表映射"""
    # def get_queryset(self): # 重写获取原始数据的方法
    #     """更改查询集"""
    #     return super(BookInfoManager, self).get_queryset().filter('isDelete=False')  # 先调用父类的方法查到最原始的数据后，再进行过滤

    def create(self,btitle,bpub_date):
        """在自定义的管理器中定义模型类对象的创建方法"""
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


# Create your models here.
# 模型类--对应数据库中的表
class BookInfo(models.Model): # 模型类中的__init__不能用了
    """图书信息类"""
    btitle = models.CharField(max_length=100) # 定义一般书名字段
    bpub_date = models.DateTimeField(db_column='pub_date') # 定义日期字段，设置默认字段名与类属性名不同
    bread = models.IntegerField(default=10) # 定义阅读量字段，并设置默认值
    bcommet = models.IntegerField(null=False) # 定义描述字段，默认不可为空
    isDelete = models.BooleanField(default=False) # 定义逻辑删除
    # 元选项
    class Meta:
        db_table = 'bookinfo' # 修改表的名字
    books1 = models.Manager() # 默认的资源管理器
    books2 = BookInfoManager() # 定义自定义的资源管理器对象（将管理器的对象作为，模型类的属性）

    @classmethod
    def create(cls,btitle,bpub_date):
        """模型类中定义创建方法
            也可以在自定义的管理器中定义
            用法：
                b=BookInfo.create('qwe',datetime(2017,1,1))
                b.save()
        """
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class HeroInfo(models.Model):
    """英雄角色类"""
    hname = models.CharField(max_length=100) # 名字
    hgender = models.BooleanField(default=True) # 性别
    hcontent = models.CharField(max_length=100) # 描述
    isDelete = models.BooleanField(default=False) # 逻辑删除
    book = models.ForeignKey('BookInfo','on_delete=models.CASCADE') # 定义外键

    def __str__(self):
        return self.hname