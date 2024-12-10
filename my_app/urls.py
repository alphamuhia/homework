from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('home/', views.home, name="home.html"),
    path('about/', views.about, name="about.html")
]