from django.urls import path
from django.conf.urls import url, include

from . import views


app_name = 'users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('my-account/', views.account, name='account'),
     path('logout/', views.logout, name='logout'),
]








