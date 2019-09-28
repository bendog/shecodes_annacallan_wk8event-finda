from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from eventFinderApp import viewsets


from . import views


app_name = 'eventFinderApp'

urlpatterns = [
    # event-finder/
    path('', views.IndexView.as_view(), name='index'),
    # event-finder/1
    path('<int:pk>/', views.EventView.as_view(), name='event'),
    # event-finder/my-account
    path('new-event/', views.NewEventView.as_view(), name='event_adder'),
    path('thanks/', views.thanks, name='thanks'),
]