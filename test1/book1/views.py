from django.shortcuts import render
from django.template import loader,RequestContext
from .models import bookInfo,heroinfo
# Create your views here.
from  django.http import HttpResponse
def index(response):
    # # 加载模板
    # template=loader.get_template('bookhtml/index.html')
    # #构造
    # context={'name':111}
    # #渲染模板
    # result=template.render(context)
    # #返回模板
    # return HttpResponse(result)
    return render(response,'bookhtml/index.html',{'name':'zzy'})
def list(response):
    # # 加载模板
    # template=loader.get_template('bookhtml/list.html')
    # allbook=bookInfo.objects.all()
    # # 构造
    # context={'allbook':allbook}
    # # 渲染模板
    # result=template.render(context)
    # # 返回模板
    # return HttpResponse(result)
    return  render(response,'bookhtml/list.html',{'allbook':bookInfo.objects.all()})
def detail(reponse,id):
    try:

        book = bookInfo.objects.get(pk=id)

        # return HttpResponse('detail')
    except Exception as e:
        return  HttpResponse('没有该书籍')

    #     # 加载模板
    # template = loader.get_template('bookhtml/detail.html')
    #
    # #     # #构造上下文
    # context = {'book': book}
    # # 渲染模板
    # result = template.render(context)
    # return HttpResponse(result)

    return  render(reponse,'bookhtml/detail.html',{'book':bookInfo.objects.get(pk=id)})