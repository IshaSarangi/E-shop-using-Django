from django.contrib import admin
from django.urls import path
from .Views import home, login, signup
# from .Views.home import index
# from .Views.signup import Signup
# from .Views.login import Login

urlpatterns = [
    path('', home.index, name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(), name='login')
]
