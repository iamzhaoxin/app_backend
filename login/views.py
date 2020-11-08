import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import User


def registered(request):
    if not request.method == "POST":
        return HttpResponse('-1')  # 未使用POST访问

    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    img = request.FILES.get('file')
    identity = request.POST.get('identity')

    if User.objects.filter(id__exact=id):
        return HttpResponse('1')  # 用户id已被注册
    else:
        User.objects.create(id=id, name=name, password=password, image_path=img, identity=identity)
        return HttpResponse('0')  # 注册成功


def login(request):
    if not request.method == "POST":
        return HttpResponse('-1')  # 未使用POST访问

    id = request.POST.get('id')
    password = request.POST.get('password')

    passw = User.objects.filter(id=id)

    if not passw:
        return HttpResponse('1')  # 用户id不存在
    elif password == passw[0].password:
        return HttpResponse('0')  # 登陆成功
    else:
        return HttpResponse('2')  # 密码错误


def change_name(request):
    if not request.method == "POST":
        return HttpResponse('-1')  # 未使用POST访问

    id = request.POST.get('id')
    name = request.POST.get('name')

    if not User.objects.filter(id=id):
        return HttpResponse('1')  # 用户id不存在

    user = User.objects.get(id=id)
    user.name = name;
    user.save()

    if User.objects.filter(id=id)[0].name == name:
        return HttpResponse('0')  # name修改成功
    else:
        return HttpResponse('2')  # 查询到name修改失败


def change_password(request):
    if not request.method == "POST":
        return HttpResponse('-1')  # 未使用POST访问

    id = request.POST.get('id')
    password = request.POST.get('password')

    if not User.objects.filter(id=id):
        return HttpResponse('1')  # 用户id不存在

    user = User.objects.get(id=id)
    user.password = password;
    user.save()

    if User.objects.filter(id=id)[0].password == password:
        return HttpResponse('0')  # password修改成功
    else:
        return HttpResponse('2')  # 查询到password修改失败


def change_img(request):
    if not request.method == "POST":
        return HttpResponse('-1')  # 未使用POST访问

    id = request.POST.get('id')
    img = request.FILES.get('file')

    if not User.objects.filter(id=id):
        return HttpResponse('1')  # 用户id不存在

    user = User.objects.get(id=id)
    user.image_path = img;
    user.save()

    return HttpResponse('0')  # 头像修改成功
