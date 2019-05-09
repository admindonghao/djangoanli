from django.conf.urls import url
from . import views

app_name = 'storeproject'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^quit/$', views.quit, name='quit'),
    url(r'^login/$', views.login_s, name='login_s'),
    url(r'^classifys/(\d+)/$', views.classifys, name='classifys'),
    url(r'^tags/(\d+)/$', views.tags, name='tags'),
    url(r'^brands/(\d+)/$', views.brands, name='brands'),
    url(r'^discount/$', views.discount, name='discount'),
    url(r'^details/(\d+)/$', views.details, name='details'),
    url(r'^view_cart/$', views.view_cart, name='view_cart'),
    url(r'^add_cart/(\d+)/$', views.add_cart, name='add_cart'),
    url(r'^clear_cart/$', views.clear_cart, name='clear_cart'),
]