from django.conf.urls import url
from .views import auth_login, profile
from django.urls import path

urlpatterns = [
    path('login/', auth_login, name='auth_login'),
    path('profile/', profile, name='profile'),
]
