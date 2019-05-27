from django.shortcuts import render

# Create your views here.
#
from .models import *
#
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
    questions=Question.objects.all()
    # return render(request,'ttt/index.html',{})
    print('请求的方法是：',request.method)
    print('向web端发送全部数据：',locals())
    # locals向模板传输该方法里所有的信息
    # 结果是：{'questions': <QuerySet [<Question: 今天吃什么>]>, 'request': <WSGIRequest: GET '/polls/index/'>}
    # 渲染
    return render(request, 'ttt/index.html', locals())


def detail(request,id):
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



def result(request,id):
    question=  Question.objects.get(pk=id)

    return render(request,'ttt/result.html',locals())