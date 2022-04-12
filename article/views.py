from django.shortcuts import render
from .models import ArticlePost
from django.http import HttpResponse
import markdown
from django.shortcuts import redirect
from django.urls import reverse
from userprofile.models import BlogUser
# Create your views here.

def index(request):
    ob = ArticlePost.objects.filter(status=1)
    context = {"articles" : ob}
    return render(request,"article/index.html",context)

def articleDetail(request,aid=0):
    aob = ArticlePost.objects.get(id=aid)
    aob.body = markdown.markdown(aob.body,
        extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        ])
    
    uob = BlogUser.objects.get(id=aob.author)
    aob.articleAuthor = uob.name

    context = {"article":aob}
    return render(request,"article/detail.html",context)

#新增修改文章操作
def articleWrite(request,aid=0):
    if aid==0 :
        # return render(request,"article/write.html")
        context = {}
    else:
        aob = ArticlePost.objects.get(id=aid)
        context = {"article":aob}
    return render(request,"article/write.html",context)

def articleSave(request,aid=0):
    if request.method == "POST": #验证提交方式是不是POST.防止用户直接访问save页面
        title = request.POST['title']
        # print(title)
        body = request.POST['body']
        # print(body)
        if title == '':
            return HttpResponse("未写标题!")
        elif body == '':
            return HttpResponse("内容为空!")
        if aid==0:
            aob = ArticlePost()
            aob.author = ArticlePost.objects.get(id=1).author
            aob.title = title
            aob.body = body 
            aob.save()
        else:
            aob = ArticlePost.objects.get(id=aid)
            aob.title = title
            aob.body = body 
            aob.save()
        return redirect(reverse("article_index"))

    else:
        return HttpResponse("404")

def articleDelete(request,aid=0):
    if request.method == 'POST':
        aob = ArticlePost.objects.get(id=aid)
        aob.status = 2
        aob.save()
        return redirect(reverse("article_index"))
    else:
        return HttpResponse("非法删除")