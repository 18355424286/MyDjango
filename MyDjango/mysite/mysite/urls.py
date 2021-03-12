"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from . import views

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('mgr/', include('mgr.urls')),
    path('approvals/', include('approvals.urls')),
    path('page1/', views.page1_view),
    path('page<int:n>', views.page_view),
    path('', views.index_view),
    path('gea/', views.return_a),
    path('login', views.login_view),
    path('test', views.mytemp_view),
    path('MyCal', views.my_cal_view),
    path('TestFor', views.for_view),
    path('sport', views.sport_view, name='sport'),
    path('music/', include('music.urls'))
]
