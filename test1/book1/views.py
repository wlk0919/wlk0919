from django.shortcuts import render
from django.template import loader,RequestContext
from .models import bookInfo,heroinfo
# Create your views here.
from  django.http import HttpResponse,HttpResponseRedirect
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
def deletebook(response,id):
    book=bookInfo.objects.get(pk=id)
    # heroid=book.heroinfo_set.id
    book.delete()
    # return HttpResponse('success')
    return HttpResponseRedirect('/book1/list/')
def deletehero(response,id):
    hero=heroinfo.objects.get(pk=id)
    bookid=hero.book.id
    hero.delete()
    # return HttpResponse('success')
    return  HttpResponseRedirect('/book1/detail/%s/'%(bookid,))
def addhero(response,id):
    if response.method=='GET':
        return render(response, 'bookhtml/addhero.html',{'bookid':id})
    elif response.method=='POST':
        book=bookInfo.objects.get(pk=id)
        print('book',book)
        hero=heroinfo()
        hero.name=response.POST['username']
        value=response.POST['sex']
        print('value',value)
        hero.ender=value
        hero.content=response.POST['content']
        hero.book=book
        hero.save()
        return  HttpResponseRedirect('/book1/detail/%s'%(id,))
    # return HttpResponse('success')
def updatehero(response,id):
    if response.method=='Post':
        book=bookInfo.objects.get(pk=id)
        hero = heroinfo()
        hero.name = response.POST['username']
        value = response.POST['sex']
        hero.ender = value
        hero.content = response.POST['content']
        hero.book = book
        allheroname=book.heroinfo_set.all().name
        print(allheroname)


        # hero.save()
        return HttpResponse('success')