from django.contrib import admin
from django.urls import path
#
from . import views
from django.conf.urls import  url
app_name='polls'
urlpatterns = [
    url(r'^login/$',views.login,name='login'),
    url(r'^index/$',views.index ,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result ,name='result'),
    url(r'^loginout/%',views.loginout,name='loginout'),
    url(r'^hhh/$',views.hhh,name='hhh'),
    url(r'^regist/$',views.regist,name='regist')

]