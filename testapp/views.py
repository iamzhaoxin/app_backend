import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from testapp.models import test


def hello(request):
    dtime = datetime.datetime.now().strftime("%d%H%M%S")  # 获取当前时间并转化为字符串作为id，因为id自动当选主键，唯一值！

    k = test.objects.create(name="zhaoxin", id=dtime)  # 插入数据库
    if k:
        dres = '数据库添加成功2,id=' + dtime
    else:
        dres = '数据库添加失败3'
    if request.method == "POST":
        name = request.POST.get('name')
        res = ['Hi~', name]
    else:
        res = 'Hi~,you are using "get" to visit this website'
    return HttpResponse((dres + res))  # json.dumps(res) : 返回json格式
