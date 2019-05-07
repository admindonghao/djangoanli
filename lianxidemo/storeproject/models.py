from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# 用户，继承系统自带的用户表
class Users(AbstractUser):
    qq = models.IntegerField(blank=True, null=True, verbose_name='QQ号码')
    plone = models.IntegerField(blank=True, null=True, verbose_name='手机号码')


# 标签表
class Labels(models.Model):
    name = models.CharField(max_length=10, verbose_name='标签')


# 大类
class Big_Class(models.Model):
    name = models.CharField(max_length=20, verbose_name='类名')


# 分类表
class Classify(models.Model):
    categories = models.ForeignKey(Big_Class, on_delete=models.CASCADE, verbose_name='大类')
    category = models.CharField(max_length=20, verbose_name='种类')
    rank = models.IntegerField(default=1, verbose_name='排列顺序')
    sex = models.BooleanField(default=0, verbose_name='男装（默认），女装')


# 品牌
class Brands(models.Model):
    brand = models.CharField(max_length=20, verbose_name='品牌')


# 尺寸
class Sizes(models.Model):
    size = models.CharField(max_length=10, verbose_name='尺寸')


# 广告
class ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='广告标题')
    img = models.ImageField(upload_to='ad/%Y/%m', verbose_name='广告图片路径')
    data = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    rank = models.ImageField(default=1, verbose_name='排列顺序')


# 商品表
class Goods(models.Model):
    classify = models.ForeignKey(Classify, on_delete=models.CASCADE, verbose_name='分类')
    name = models.CharField(max_length=50, verbose_name='商品名称')
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name='品牌')
    sizes = models.ManyToManyField(Sizes, verbose_name='尺寸')
    priceed = models.IntegerField(default=0.0, verbose_name='原价')
    price = models.IntegerField(default=0.0, verbose_name='现价')
    abstract = models.TextField(verbose_name='简介')
    sales = models.IntegerField(default=0, verbose_name='销量')
    inventory = models.IntegerField(default=1, verbose_name='库存')
    show_picture = models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg', verbose_name='展示图片路径')
    details_picture_1 = models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg',
                                          verbose_name='详情图片路径1')
    details_picture_2 = models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg',
                                          verbose_name='详情图片路径2')
    details_picture_3 = models.ImageField(upload_to='clothing/%Y/%m', default='clothing/default.jpg',
                                          verbose_name='详情图片路径3')
    shop_cart_picture = models.ImageField(upload_to='clothing/%Y/%m', default='clothing/ce.jpg',
                                          verbose_name='购物车中的图片')

