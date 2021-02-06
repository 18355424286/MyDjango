from django.db import models
from django.contrib import admin

# Create your models here.


class Customer(models.Model):
    # 客户姓名
    name = models.CharField(max_length=200)

    # 联系电话
    phone_number = models.CharField(max_length=200)

    # 地址
    address = models.CharField(max_length=200)

    # qq
    qq = models.CharField(max_length=20, null=True, blank=True)
    pass


admin.site.register(Customer)
