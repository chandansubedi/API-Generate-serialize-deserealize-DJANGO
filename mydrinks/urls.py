from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('drink',views.drink_list,name='drink_list'),
    path('drink/<int:id>',views.drink_details,name='drink_details'),
]