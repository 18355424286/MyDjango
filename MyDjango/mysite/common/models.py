from django.db import models
from django.contrib import admin
import datetime

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


class Medicine(models.Model):
    # 药品名
    name = models.CharField(max_length=50)

    # 药品编号
    sn = models.CharField(max_length=50)

    # 描述
    desc = models.CharField(max_length=200)
    pass


class Order(models.Model):
    # 订单编号
    order_id = models.CharField(max_length=20)

    # 创建日期
    create_data = models.DateField(default=datetime.datetime.now())

    # 申请人
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    # on_delete是当删除主表中的记录时的处理方案
    # CASCADE:删除主键记录和相应的关联记录
    # PROTECT:禁止删除
    # SET_NULL:删除主键记录，并且将相关字段设置为NULL

    # 药品
    medicines = models.ManyToManyField(Medicine, through="OrderMedicine")
    # 表间关系
    # ForeignKey:一对多
    # OneToOneField:一对一
    # ManyToManyField:多对多
    pass


class OrderMedicine(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)

    # 药品数量
    amount = models.PositiveIntegerField()


admin.site.register(Recharge)
admin.site.register(Customer)
