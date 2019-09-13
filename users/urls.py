from django.urls import path
from django.conf.urls import url, include

from . import views


app_name = 'users'

urlpatterns = [
path('register/', views.Register.as_view(), name='register'),
path('users/', include('django.contrib.auth.urls')),
]








