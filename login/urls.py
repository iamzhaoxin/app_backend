from django.urls import path

from login.views import registered, login, change_name, change_password, change_img

# 前路由：path('login/',include('login.urls')),
urlpatterns = [
    path('registered', registered),
    path('login', login),
    path('changename', change_name),
    path('changepassword', change_password),
    path('changeimg', change_img),
]
