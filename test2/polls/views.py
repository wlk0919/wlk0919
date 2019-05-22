from django.shortcuts import render,get_list_or_404
from django.http import HttpResponse
from .models import Article
# 引用分页器
from django.core.paginator import Paginator
import markdown
# Create your views here.
def index(request):

    pagenum=request.GET.get('page')
    if pagenum==None:
        pagenum=1
    else:
        pagenum=pagenum
    # 获取所有文章
    articles=Article.objects.all().order_by('-views')
    # 每页一个文章
    paginator=Paginator(articles,1)
    # 页码
    page=paginator.get_page(pagenum)
    return render(request,'index.html',{'page':page})

def detail(request,id):
    article=get_list_or_404(Article,pk=id)
    mk=markdown.Markdown(extensions=[
        "markdown.extensions.extra",
        "markdown.extensions.codehilite",
        "markdown.extensions.toc"
    ])
    # 吧Markdown格式连载为html格式
    article.body=mk.convert(article.body)
    article.toc=mk.toc
    # locals（）传输所有数据
    return render(request,'single.html',locals())