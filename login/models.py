from django.db import models

# Create your models here.
from django.utils.baseconv import base64


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    image_path = models.ImageField(upload_to='images')
    identity = models.CharField(max_length=20, default="")


class Info:
    def __init__(self, ID):
        self.status = 0
        self.id = ID
        if User.objects.filter(id__exact=self.id):
            self.status = 1  # 用户id已被注册
        else:
            self.status = 2  # id未注册

    def get_info(self):
        user = User.objects.get(id=self.id)
        data = {
            'id': user.id,
            'name': user.name,
            'img': str(user.image_path),  # 怎么传图片呢……用图床？或者得到路径后再来一个get的request？
            'identity': user.identity
        }
        return data

    def get_password(self):
        return User.objects.get(id=self.id).password

    def get_name(self):
        return User.objects.get(id=self.id).name

    def get_img(self):
        return User.objects.get(id=self.id).image_path
