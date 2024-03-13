from django.urls import path
from . import views

urlpatterns = [
    path('P1', views.P1Page, name='P1Page'),
    path('P2', views.P2Page, name='P2Page'),
    path('P3', views.P3Page, name='P3Page'),
    path('P4', views.P4Page, name='P4Page'),
    path('Trans', views.TransPage, name='TransPage'),
    path('TSO', views.TSOPage, name='TSOPage'),
]