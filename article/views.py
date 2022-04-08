from django.shortcuts import render
from .models import ArticlePost
# Create your views here.

def index(request):
    ob = ArticlePost.objects.all()
    context = {"articles" : ob}
    return render(request,"article/index.html",context)

def articleDetail(request,aid=0):
    aob = ArticlePost.objects.get(id=aid)
    context = {"article":aob}
    return render(request,"article/detail.html",context)