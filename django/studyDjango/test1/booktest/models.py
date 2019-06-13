from django.db import models

# Create your models here.
class BookInfo(models.Model):
    """创建书本信息类"""
    btitle=models.CharField(max_length=20) # 书名
    bpub_date=models.DateTimeField() # 日期

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """创建英雄信息类"""
    hname=models.CharField(max_length=10) # 英雄名
    hgender=models.BooleanField() # 性别
    hcontent=models.CharField(max_length=1000) # 内容
    hbook=models.ForeignKey('BookInfo', 'on_delete=models.CASCADE') # 引用外键，即BookInfo对象

    def __str__(self):
        return self.hname