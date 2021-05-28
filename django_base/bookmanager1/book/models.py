# coding=utf8
from django.db import models


# Create your models here.

class Bookinfo(models.Model):
    name = models.CharField(max_length=10, unique=True)
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改mysql表名, 不修改导入报错
        verbose_name = '书籍管理'  # admin站点使用的(liaojie)

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.name


class Peopleinfo(models.Model):
    # 定义一个有序字典
    GENDER = ((1, 'male'), (0, 'female'))

    name = models.CharField(max_length=20, unique=True)
    gender = models.SmallIntegerField(choices=GENDER, default=0)
    description = models.CharField(max_length=200, null=True)
    is_delete = models.BooleanField(default=False)
    book = models.ForeignKey(Bookinfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'
        verbose_name = '人物信息'

    def __str__(self):
        return self.name + str(self.id)