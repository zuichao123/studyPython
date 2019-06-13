from django.db import models
from tinymce.models import HTMLField


class UserInfo(models.Model):
    uname = models.CharField(max_length=10)
    upwd = models.CharField(max_length=40)
    isDelete = models.BooleanField()


# 模型类--对应数据库中的表
class BookInfo(models.Model): # 模型类中的__init__不能用了
    """图书信息类"""
    btitle = models.CharField(max_length=100) # 定义一般书名字段
    bpub_date = models.DateTimeField(db_column='pub_date') # 定义日期字段，设置默认字段名与类属性名不同
    bread = models.IntegerField(default=10) # 定义阅读量字段，并设置默认值
    bcommet = models.IntegerField(null=False) # 定义描述字段，默认不可为空
    isDelete = models.BooleanField(default=False) # 定义逻辑删除


class HeroInfo(models.Model):
    """英雄角色类"""
    hname = models.CharField(max_length=100) # 名字
    hgender = models.BooleanField(default=True) # 性别
    hcontent = models.CharField(max_length=100) # 描述
    isDelete = models.BooleanField(default=False) # 逻辑删除
    book = models.ForeignKey('BookInfo','on_delete=models.CASCADE') # 定义外键


class AreaInfo(models.Model):
    """分页类
        create table booktest_areainfo(
        id int primary key not null auto_increment,
        title varchar(10),
        parea_id int,
        foreign key(parea_id) references booktest_areainfo(id)
         );
    """
    title = models.CharField(max_length=20)
    parea = models.ForeignKey('self', 'on_delete=models.CASCADE') # 自关联


# 创建这三个表的语句详见鄙人博客：https://www.cnblogs.com/zuichao/p/10962046.html
class Province(models.Model):
    provinceID = models.CharField(max_length=10)
    province = models.CharField(max_length=50)


class City(models.Model):
    cityID = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    father = models.CharField(max_length=10)


class Area(models.Model):
    areaID = models.CharField(max_length=50)
    area = models.CharField(max_length=60)
    father = models.CharField(max_length=10)


# 富文本编辑器模型类
class Test1(models.Model):
    content = HTMLField()