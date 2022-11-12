from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.home, name='home'),
    path('acessibilidade/', views.acessibilidade, name='acessibilidade'),
]