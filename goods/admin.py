from django.contrib import admin

from .models import Goods, GoodsCategory, GoodsCategoryBrand, Banner, HotSearchWords, IndexAd


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ("name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                    "shop_price", "goods_brief", "goods_desc", "is_new", "is_hot", "add_time")
    search_fields = ['name', ]
    list_editable = ["is_hot", ]
    list_filter = ["name", "click_num", "sold_num", "fav_num", "goods_num", "market_price",
                   "shop_price", "is_new", "is_hot", "add_time", "category__name"]
    style_fields = {"goods_desc": "ueditor"}


@admin.register(GoodsCategory)
class GoodsCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "category_type", "parent_category", "add_time"]
    list_filter = ["category_type", "parent_category", "name"]
    search_fields = ['name', ]


@admin.register(GoodsCategoryBrand)
class GoodsCategoryBrandAdmin(admin.ModelAdmin):
    list_display = ["category", "image", "name", "desc"]


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ["goods", "image", "index"]


@admin.register(HotSearchWords)
class HotSearchWordsAdmin(admin.ModelAdmin):
    list_display = ["keywords", "index", "add_time"]


@admin.register(IndexAd)
class IndexAdAdmin(admin.ModelAdmin):
    list_display = ["category", "goods"]
