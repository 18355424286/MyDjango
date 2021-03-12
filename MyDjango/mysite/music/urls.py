from django.urls import path
from . import views


urlpatterns = [
    path('page1', views.page1_view),
    path('page2', views.page2_view),
    path('page3', views.page3_view),
]
