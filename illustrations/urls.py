
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('artists/', views.artists, name="artists"),
    path('contact/', views.contact, name="contact"),
    path('illustrations/', views.illustrations, name="illustrations"),
    path('create_doodle/', views.create_doodle, name="create_doodle"),
    path('<int:doodle_id>/delete/doodle_confirm_delete/', views.delete_doodle, name="delete_doodle"),
    path('register/', views.register, name="register")
]
