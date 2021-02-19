from django.urls import path

from SistGoyApp import views

#urls del SistGoyApp

urlpatterns = [
    path('',views.inicio,name='Inicio'),

]