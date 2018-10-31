from django.conf.urls import url
from .views import login
from django.urls import path

urlpatterns = [
    path('login/', login, name='login'),
]
