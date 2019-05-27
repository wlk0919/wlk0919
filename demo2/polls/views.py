from django.shortcuts import render

# Create your views here.
from .models import *

from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.


def index(request):
    questions=Question.objects.all()
    # return render(request,'ttt/index.html',{})
    print(locals())
    # locals向模板传输该方法里所有的信息
    # 结果是：{'questions': <QuerySet [<Question: 今天吃什么>]>, 'request': <WSGIRequest: GET '/polls/index/'>}
    return render(request, 'ttt/index.html', locals())


def detail(request,id):
    question=Question.objects.get(pk=id)
    print("111",request.method)
    if request.method=='POST':
        print("=======")
        # choice要和detail。html中的单选框命名name的值
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