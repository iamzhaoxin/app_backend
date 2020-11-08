import os

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from login.models import User


def test_image(request):

    User.objects.create(id=1,name='a',password='b',image_path=request.FILES.get('file'))

    return HttpResponse('ok')