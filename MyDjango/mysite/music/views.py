from django.shortcuts import render

# Create your views here.
# file:music/views.py
from django.http import HttpResponse
import pytest
import sys
import os
sys.path.append("./test_dir")


def page1_view(request):
    os.system(r'python E:\MyDjango\mysite\music\test_dir\test_login.py')
    return HttpResponse("页面1")


def page2_view(request):
    return HttpResponse('页面2')


def page3_view(request):
    return HttpResponse('页面3')
