from django.contrib import admin
from django.urls import path
#
from . import views
from django.conf.urls import  url
app_name='polls'
urlpatterns = [
    url(r'^index/$',views.index ,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result ,name='result'),

]