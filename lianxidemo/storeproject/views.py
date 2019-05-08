from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import PageNotAnInteger,InvalidPage,EmptyPage,Paginator
from django.contrib.auth import logout, login, authenticate
from .models import *
from .forms import *


# Create your views here.
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
    return locals()


# 主页界面的视图函数
def index(request):
    ad_list = Ad.objects.all()
    clo_list = Goods.objects.all()
    clo_list = getPage(request,clo_list)
    category_list = global_setting(request)
    print(category_list['category_list_m'])
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
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login(request, user)
            else:
                return render(request, 'error.html', {'reason': '登录验证失败'})
            return redirect(request.POST['source_url'])
        else:
            return render(request, 'store/error.html', {'reasom':login_form.errors})


# 退出
def quit(request):
    return HttpResponse('已退出')

