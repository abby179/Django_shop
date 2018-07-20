from django.contrib import admin

from .models import ShoppingCart, OrderGoods, OrderInfo


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ["user", "goods", "nums"]


class OrderGoodsInline(admin.TabularInline):
    model = OrderGoods
    exclude = ['add_time', ]


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    list_display = ["user", "order_sn",  "trade_no", "pay_status", "post_script", "order_mount",
                    "order_mount", "pay_time", "add_time"]
    inlines = [OrderGoodsInline, ]



