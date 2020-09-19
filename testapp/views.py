import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello(request):
    if request.method=="POST":
        name=request.POST.get('name')
        res=['Hi~',name]
    else:
        res='Hi~,you are using "get" to visit this website'
    return HttpResponse((res))  #json.dumps(res) : 返回json格式