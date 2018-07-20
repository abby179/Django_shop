from datetime import datetime

from django.db import models

from ckeditor.fields import RichTextField


class GoodsCategory(models.Model):
    """
    multi-category of goods
    """
    CATEGORY_TYPE = (
        (1, "first class"),
        (2, "second class"),
        (3, "third class"),
    )

    name = models.CharField(default="", max_length=30, help_text="category_name")
    code = models.CharField(default="", max_length=30, help_text="category_code")
    desc = models.TextField(default="", help_text="category_description")
    category_type = models.IntegerField(choices=CATEGORY_TYPE, help_text="category_type")
    parent_category = models.ForeignKey("self", null=True, blank=True, help_text="parent_category",
                                        related_name="sub_cat", on_delete=models.CASCADE)
    is_tab = models.BooleanField(default=False, help_text="is_tab")
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class GoodsCategoryBrand(models.Model):
    """
    brand under a good category
    """
    category = models.ForeignKey(GoodsCategory, related_name="brands", null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=30, help_text="brand_name")
    desc = models.CharField(default="", max_length=200, help_text="brand_description")
    image = models.ImageField(max_length=200, upload_to="brands/")
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    Goods
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE)
    goods_sn = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=100)
    click_num = models.IntegerField(default=0)
    sold_num = models.IntegerField(default=0)
    fav_num = models.IntegerField(default=0)
    goods_num = models.IntegerField(default=0)
    market_price = models.FloatField(default=0)
    shop_price = models.FloatField(default=0)
    goods_brief = models.TextField(max_length=500)
    goods_desc = RichTextField(default="")
    ship_free = models.BooleanField(default=True)
    goods_front_image = models.ImageField(upload_to="goods/images", null=True, blank=True)
    is_new = models.BooleanField(default=False)
    is_hot = models.BooleanField(default=False)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    image of goods on goods details page
    """
    goods = models.ForeignKey(Goods, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", null=True, blank=True)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    banner images on homepage
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="banner")
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.goods.name


class IndexAd(models.Model):
    """
    ads under category on homepage
    """
    category = models.ForeignKey(GoodsCategory, related_name="ads", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name='ads')

    def __str__(self):
        return self.goods.name


class HotSearchWords(models.Model):
    """
    hot search words under search box on homepage
    """
    keywords = models.CharField(max_length=20, default="")
    index = models.IntegerField(default=0)
    add_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.keywords

