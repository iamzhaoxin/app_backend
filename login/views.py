import json
import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import User, Info


def registered(request):
    res = HttpResponse()

    if not request.method == "POST":
        res.status_code = 400
        res.content = '-1'  # 未使用POST访问
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        img = request.FILES.get('file')
        identity = request.POST.get('identity')

        a = Info(id)

        if a.status == 1:
            res.status_code = 400
            res.content = '1'  # id已被注册
        else:
            User.objects.create(id=id, name=name, password=password, image_path=img, identity=identity)
            res.status_code = 200
            res.content_type = "application/json"
            res.content = json.dumps(a.get_info())

    return res


def login(request):
    res = HttpResponse()

    if not request.method == "POST":
        res.status_code = 400
        res.content = '-1'  # 未使用POST访问
    else:
        id = request.POST.get('id')
        password = request.POST.get('password')

        a = Info(id)
        if a.status == 2:
            res.status_code = 400
            res.content = '1'  # 用户未注册
        elif password == a.get_password():
            res.status_code = 200
            res.content_type = "application/json"
            res.content = json.dumps(a.get_info())
        else:
            res.status_code = 400
            res.content = '2'  # 密码错误

    return res


def change_name(request):
    res = HttpResponse()

    if not request.method == "POST":
        res.status_code = 400
        res.content = '-1'  # 未使用POST访问
    else:
        id = request.POST.get('id')
        name = request.POST.get('name')

        a = Info(id)
        if a.status == 2:
            res.status_code = 400
            res.content = '1'  # 用户未注册
        else:
            user = User.objects.get(id=id)
            user.name = name;
            user.save()

            if a.get_name() == name:
                res.status_code = 200
                res.content_type = "application/json"
                res.content = json.dumps(a.get_info())
            else:
                res.status_code = 400
                res.content = '2'  # 查询到name修改失败

    return res


def change_password(request):
    res = HttpResponse()

    if not request.method == "POST":
        res.status_code = 400
        res.content = '-1'  # 未使用POST访问
    else:
        id = request.POST.get('id')
        password = request.POST.get('password')

        a = Info(id)
        if a.status == 2:
            res.status_code = 400
            res.content = '1'  # 用户未注册
        else:
            user = User.objects.get(id=id)
            user.password = password
            user.save()

            if a.get_password() == password:
                res.status_code = 200
                res.content_type = "application/json"
                res.content = json.dumps(a.get_info())
            else:
                res.status_code = 400
                res.content = '2'  # 查询到password修改失败

    return res


def change_img(request):
    res = HttpResponse()

    if not request.method == "POST":
        res.status_code = 400
        res.content = '-1'  # 未使用POST访问
    else:
        id = request.POST.get('id')
        img = request.FILES.get('file')

        a = Info(id)
        if a.status == 2:
            res.status_code = 400
            res.content = '1'  # 用户未注册
        else:
            user = User.objects.get(id=id)
            user.image_path = img
            user.save()

            if a.get_img() == img:
                res.status_code = 200
                res.content_type = "application/json"
                res.content = json.dumps(a.get_info())
            else:
                res.status_code = 400
                res.content = '2'  # 查询到img修改失败

    return res
