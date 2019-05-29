from django.shortcuts import render,redirect,reverse

# Create your views here.
#导入模型类
from .models import *
#
from django.http import HttpResponse,HttpResponseRedirect
# 引入Django自带的登录，登出  autenticate授权
from django.contrib.auth import authenticate,login as lgi,logout as lgo


# Create your views here.
def hhh(request):
    res=HttpResponse()

    # res.set_cookie('username', 'aaa')
    # 使用session登录
    request.session['username'] = 'aaa'

    # print('cookies:  ',request.COOKIES)
    # print('sss:   ',res)
    # return res
    return redirect('/login')

def login(request):
    print('////////')
    print(request.method)
    # 这是自己写的方法
    # if request.method=='GET':
    #     return render(request,'ttt/login.html')
    # else:
    #     # res = HttpResponse('index')
    #     # res.set_cookie('username', 'aaa')
    #     # 使用session
    #     print(request.session)
    #     # 获取可以根据输入框内的值，获取
    #     request.session["username"] = request.POST.get('username')
    #     username = request.session.get('username')
    #     # 使用cookie
    #     # username = request.COOKIES.get('username')
    #     print(username)
    #
    #     # print(request.COOKIES)
    #
    #     # pwd=request.POST.get('password')
    #     if username=='aaa':
    #         # 重定向到index页面
    #
    #         return  redirect(reverse('polls:index'))
    #     else:
    #         # 重新回到登录页面
    #         return render(request,'ttt/login.html')
    if request.method=='POST':
#     Django自带的登录登出方法
        username=request.POST.get('username')
        pwd=request.POST.get('password')
        # 在数据库中找到用户的信息
        # 授权
        user=authenticate(request,username=username,password=pwd)
        print(user)
        # 使用session登录
        lgi(request,user)
        return redirect(reverse('polls:index'))
    else:
        return  render(request,'ttt/login.html')

def regist(request):
    if request.method=='POST':
        username=request.POST.get('username_reg')
        pwd=request.POST.get('password_reg')
        pwd2 = request.POST.get('password_reg_2')
        if pwd != pwd2:
            return render(request,'polls/login.html',{'error':'密码不一致'})
        else:
            user=myUser.objects.create_user(username=username,password=pwd,url='http://aaa123.com')
            print('信息：',user.id,user.username,user.is_active)
            print(user)
            # 默认注册用户之后为非激活状态
            # user.is_active=False
            # user.save()
            return  redirect(reverse('polls:login'))



        # return HttpResponse('注册成功')


def loginout(request):
    res=redirect(reverse('polls:login'))
    # return HttpResponse('退出成功')
    # res.delete_cookie('username')
    # res.COOKIES.flush()
    # 使用session退出
    # request.session.flush()
    # print('session方法',request.session)
    # 自带的登出方法
    lgo(request)
    return res

# 这是一个装饰器
def checklogin(fun):
    def check(request,*args):
        # 使用session登录
        un=request.session.get('username')
        print(request.user)
        # 判断是否有该用户，并且不是匿名用户
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse('polls:login'))
        # un=request.COOKIES.get('username')
        # if un:
        #     # username=un
        #     # 需要换回
        #     return fun(request,*args)
        # else:
        #     return  redirect(reverse('polls:login'))
    return check

@checklogin
def index(request):
    username =request.session.get('username')
    # username=request.COOKIES.get('username')
    # 使用session登录
    # username=request.session.get('username')
    questions=Question.objects.all()
    # return render(request,'ttt/index.html',{})
    print('请求的方法是：',request.method)
    # print('向web端发送全部数据：',locals())
    # print(request.COOKIES)
    # locals向模板传输该方法里所有的信息
    # 结果是：{'questions': <QuerySet [<Question: 今天吃什么>]>, 'request': <WSGIRequest: GET '/polls/index/'>}
    # 渲染
    return render(request, 'ttt/index.html', locals())


@checklogin
def detail(request,id):
    username = request.session.get('username')
    # username=request.COOKIES.get('username')
    question=Question.objects.get(pk=id)
    # 之前的request方法都是GET
    print("111",request.method)
    # form表单，提交后的方法变为POST方法
    if request.method=='POST':
        print("=======")#多用print来进行调试
        # choice是提交选项时的name值
        c_id=request.POST.get("choice")
        choice=Choice.objects.get(pk=c_id)
        print(choice.votes)
        # 也可以新建一个管理器
        choice.votes+=1
        print(choice.votes)
        # print('票数是:  ',choice.votes)
        choice.save()
        return HttpResponseRedirect('/polls/result/%s/'%(id,))
    else:
        return render(request,'ttt/detail.html',locals())


@checklogin
def result(request,id):
    username = request.session.get('username')
    # username = request.COOKIES.get('username')
    question=  Question.objects.get(pk=id)

    return render(request,'ttt/result.html',locals())