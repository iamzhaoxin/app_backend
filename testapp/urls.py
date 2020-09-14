from django.urls import path

from testapp.views import hello

urlpatterns = [
    path('hello/', hello),
]
