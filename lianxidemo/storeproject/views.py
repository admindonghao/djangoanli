from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import PageNotAnInteger,InvalidPage,EmptyPage,Paginator
from django.contrib.auth import logout, login, authenticate
# from django.core import serializers
from django.db.models import F
from .models import *
from .forms import *


# Create your views here.
# 购物车相关的装饰器
def authenticated_view(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return function(request)
        else:
            login_form = LoginFrom()
            return render(request, 'store/login.html', locals())

    wrap.__doc__=function.__doc__
    wrap.__name__=function.__name__
    return wrap


def global_setting(request):
    # 站点信息
    classify_list = Classify.objects.all()
    # 男装分类
    category_list_m = [c for c in classify_list if c.sex == 0]
    # 女装分类
    category_list_f = [c for c in classify_list if c.sex == 1]
    # 品牌信息
    brand_list = Brands.objects.all()
    # 热销榜
    hot_list = Goods.objects.all().order_by('-sales')[:4]
    # 标签
    tag_list = Labels.objects.all()
    # 购物车
    cart = request.session.get(request.user.id, None)
    return locals()


# 主页界面的视图函数
def index(request):
    ad_list = Ad.objects.all()
    clo_list = Goods.objects.all()
    clo_list = getPage(request,clo_list)
    category_list = global_setting(request)
    return render(request, 'store/index.html', locals())


# 分页
def getPage(request,clo_list):
    paginator = Paginator(clo_list,8)
    try:
        page = int(request.GET.get('page',1))
        clo_list = paginator.page(page)
    except (EmptyPage,InvalidPage,PageNotAnInteger):
        clo_list = paginator.page(1)
    return clo_list


# 注册
def register(request):
    if request.method == 'GET':
        reg_form = RegFrom()
        return render(request, 'store/register.html', locals())
    elif request.method == 'POST':
        reg_form = RegFrom(request.POST)
        if reg_form.is_valid():
            user = Users()
            user.username = reg_form.cleaned_data['username']
            user.email = reg_form.cleaned_data['email']
            user.password = reg_form.cleaned_data['password']
            user.save()
            return redirect(reverse('store:index'))
        else:
            return render(request, 'store/error.html', {'reasom':reg_form.errors})


# 登录
def login_s(request):
    if request.method == 'GET':
        login_form = LoginFrom()
        return render(request, 'store/login.html', {'login_form':login_form})
    elif request.method == 'POST':
        login_form = LoginFrom(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            passworf = login_form.cleaned_data['password']
            user = authenticate(username=username, password=passworf)
            print(user)
            # return HttpResponse('登录成功')
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
            else:
                return render(request, 'store/error.html', {'reasom': '登录验证失败'})
            return redirect(request.POST['source_url'])
        else:
            return render(request, 'store/error.html', {'reasom':login_form.errors})


# 退出
def quit(request):
    logout(request)
    return redirect(reverse('store:login_s',))


# 分类列表页
def classifys(request,id):
    try:
        category = Classify.objects.get(pk=id)
    except:
        return render(request, 'store/error.html', {'reasom': '没有此分类'})
    clo_list = category.goods_set.all()
    clo_list = getPage(request, clo_list)
    category_list = global_setting(request)
    return render(request, 'store/products.html', locals())


# 标签列表页
def tags(request,id):
    try:
        tag = Labels.objects.get(pk=id)
    except:
        return render(request, 'store/error.html', {'reasom': '没有此标签'})
    clo_list = tag.goods_set.all()
    clo_list = getPage(request, clo_list)
    category_list = global_setting(request)
    return render(request, 'store/products.html', locals())


# 品牌列表页
def brands(request, id):
    try:
        brand = Brands.objects.get(pk = id)
    except:
        return render(request, 'store/error.html', {'reasom': '没有这个品牌'})
    clo_list = brand.goods_set.all()
    clo_list = getPage(request, clo_list)
    category_list = global_setting(request)
    return render(request, 'store/products.html', locals())


# 打折商品
def discount(request):
    clo_list = Goods.objects.filter(price__lt=F('priceed'))
    clo_list = getPage(request, clo_list)
    category_list = global_setting(request)
    return render(request, 'store/products.html', locals())


# 商品详细页
def details(request, id):
    try:
        clo = Goods.objects.get(pk=id)
    except:
        return render(request, 'store/error.html', {'reasom': '没有这个商品'})
    category_list = global_setting(request)
    return render(request, 'store/single.html', locals())


# 查看购物车
@authenticated_view
def view_cart(request):
    cart = request.session.get(request.user.id)
    return render(request, 'store/checkout.html', locals())
    # return HttpResponse('购物车')


# 加入购物车
def add_cart(request, id):
    try:
        try:
            goods = Goods.objects.get(pk=id)
        except:
            return render(request, 'store/error.html', {'reasom': '没有这个商品'})
        cart = request.session.get(request.user.id, None)
        if not cart:
            cart = Cart()
            cart.add(goods)
            request.session[request.user.id] = cart
        else:
            cart.add(goods)
            request.session[request.user.id] = cart
    except Exception as e:
        print(e)
    return render(request, 'store/checkout.html', locals())
    # return HttpResponse('添加到购物车')


# 清空购物车
def clear_cart(request):
    cart = Cart()
    request.session[request.user.id] = cart
    return render(request, 'store/checkout.html', locals())


