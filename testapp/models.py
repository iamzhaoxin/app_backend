from django.db import models

# Create your models here.

class test(models.Model):
    name=models.CharField(max_length=20)
    id=models.IntegerField(primary_key=True) #主键，唯一值

# 创建数据库模型类
