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


class Recharge(models.Model):
    # 流水号
    recharge_id = models.CharField(max_length=21)

    # 供应商
    supplier = models.CharField(max_length=200)

    # 充值人员
    recharge_user = models.CharField(max_length=10)

    # 充值时间
    recharge_time = models.DateTimeField(auto_now_add=True)

    # 充值方式
    recharge_way = models.CharField(max_length=5)

    # 充值金额
    recharge_money = models.DecimalField(max_digits=30, decimal_places=2)

    pass


admin.site.register(Recharge)
admin.site.register(Customer)
