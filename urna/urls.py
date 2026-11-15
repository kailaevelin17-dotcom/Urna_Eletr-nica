from django.urls import path
from . import views

urlpatterns = [
    path('', views.urna, name='urna'),
    path('resultado/', views.resultado, name='resultado'),
]