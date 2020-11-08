from django.urls import path

from login.views import registered, login

urlpatterns = [
    path('registered/', registered),
    path('',login),
]
