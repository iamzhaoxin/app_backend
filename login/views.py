import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import User


def registered(request):

    id = request.POST.get('id')
    name = request.POST.get('name')
    password = request.POST.get('password')
    img = request.FILES.get('file')
    identity = request.POST.get('identity')

    if User.objects.filter(id__exact=id):
        return HttpResponse('用户id已存在')
    else:
        User.objects.create(id=id, name=name, password=password, image_path=img, identity=identity)
        return HttpResponse('注册成功')


def login(request):
    id = request.POST.get('id')
    password = request.POST.get('password')

    passw = User.objects.filter(id=id)

    if not passw:
        return HttpResponse('用户不存在')
    elif password == passw[0].password:
        return HttpResponse('Yes')
    else:
        return HttpResponse('No')
