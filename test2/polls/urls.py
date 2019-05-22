from django.conf.urls import url
from .views import *
from . import views
app_name='polls'
urlpatterns = [

    url(r'^detail/(\d+)/$',views.detail,name='datail'),
    url(r'^$', views.index, name='index'),
]