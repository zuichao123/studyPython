from django.db import models

# Create your views here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=100)
    bpub_date = models.DateTimeField(db_column='pub_date')
    bread = models.IntegerField()
    bcommet = models.IntegerField()
    isDelete = models.BooleanField()

    class Meta():
        db_table = 'bookinfo'


class HeroInfo(models.Model):
    """英雄角色类"""
    hname = models.CharField(max_length=100) # 名字
    hgender = models.BooleanField(default=True) # 性别
    hcontent = models.CharField(max_length=100) # 描述
    isDelete = models.BooleanField(default=False) # 逻辑删除
    book = models.ForeignKey('BookInfo','on_delete=models.CASCADE') # 定义外键

    def showname(self):
        return self.hname
