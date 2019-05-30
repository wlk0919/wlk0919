from django.conf.urls import url
# 引入输入函数
from . import views
# 定义命名空间,和项目路由中的namespace一致
app_name='room'

urlpatterns=[
url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.login,name='login'),
    url(r'^index/$',views.index,name='index'),
    url(r'single/(\d+)/$',views.single,name='single'),
    url(r'^checkout/(\d+)/$',views.checkout,name='checkout'),
]

