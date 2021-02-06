from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('customers/', views.list_customers),
]