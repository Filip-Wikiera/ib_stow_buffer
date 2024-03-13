from django.urls import path
from . import views

urlpatterns = [
    path('P1', views.P1Page, name='P1Page'),
]