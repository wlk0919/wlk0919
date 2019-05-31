# render渲染，redirect重定向，reverse解除硬编码
from django.shortcuts import render,redirect,reverse
# 引入模型model类
from .models import myUser,Rooms
# 引入django自带的登录登出
from django.contrib.auth import authenticate,login as logi,logout as logo
# Create your views here.


def register(request):

    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        pwd2=request.POST.get('password2')
        if pwd!=pwd2:
            return  render(request,'ttt/register.html',{'error':'密码不一致'})
        else:
            # 返回user对象
            user=myUser.objects.create_user(username=username,password=pwd,url='http://www.aaa123.com')
            print(user)
            # return render(request, 'ttt/login.html')
            return redirect(reverse('room:login'))
    else:
        return render(request,'ttt/register.html')

def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pwd=request.POST.get('password')
#         授权
        user1=authenticate(request,username=username,password=pwd)
        logi(request,user1)
        return redirect(reverse('room:index'))
    else:
        return render(request,'ttt/login.html')
# 这是一个装饰器
def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return  redirect(reverse('room:login'))
    return check

def index(request):
    rooms=Rooms.objects.all()

    return render(request,'ttt/index.html',locals())

def single(request,id):
    room=Rooms.objects.get(pk=id)
    print('方法是  ',request.method)
    print(id)
    print('id是  ',room.id)
    if request.method=='POST':
        return  redirect(reverse('room:checkout',(id,)))
    else:
        return render(request,'ttt/single.html',locals())

def checkout(request,id):
    room=Rooms.objects.get(pk=id)
    return  render(request,'ttt/checkout.html',locals())


def contact(require):
    return render(require,'ttt/contact.html')






