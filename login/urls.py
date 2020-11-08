from django.urls import path

from login.views import test_image

urlpatterns = [
    path('test/', test_image),
]
