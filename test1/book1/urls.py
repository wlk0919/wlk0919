# 引用url
from django.conf.urls import url
# 引用视图函数
from . import views
urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^list/$',views.list),
    url(r'^detail/(\d+)/$',views.detail),
]