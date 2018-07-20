from datetime import datetime

from django.db import models
from django.contrib.auth import get_user_model

from user.models import UserProfile
from goods.models import Goods


User = get_user_model()


class ShoppingCart(models.Model):
    """
    shopping cart
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    nums = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return "{}({})".format(self.goods.name, self.nums)


class OrderInfo(models.Model):
    """
    info for one order
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", "TRADE_SUCCESS"),
        ("TRADE_CLOSED", "TRADE_CLOSED"),
        ("WAIT_BUYER_PAY", "WAIT_BUYER_PAY"),
        ("TRADE_FINISHED", "TRADE_FINISHED"),
        ("PAYING", "PAYING"),
    )
    PAY_TYPE = (
        ("alipay", "alipay"),
        ("wechat", "wechat"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # unique order number
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True)
    # random str for wechat pay
    nonce_str = models.CharField(max_length=50, null=True, blank=True, unique=True)
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True)
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30)
    pay_type = models.CharField(choices=PAY_TYPE, default="alipay", max_length=10)
    post_script = models.CharField(max_length=200)
    order_mount = models.FloatField(default=0.0)
    pay_time = models.DateTimeField(null=True, blank=True)

    # user info
    address = models.CharField(max_length=100, default="")
    signer_name = models.CharField(max_length=20, default="")
    singer_mobile = models.CharField(max_length=11)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    goods info within an order
    """
    order = models.ForeignKey(OrderInfo, on_delete=models.CASCADE, related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return str(self.order.order_sn)
