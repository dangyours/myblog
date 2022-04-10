from django.shortcuts import render
from .models import BlogUser
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.

def login(request):
    return render(request,"user/login.html")

def dologin(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        if name=='':
            context = {"nameinfo":"用户名为空"}
            return render(request,"user/login.html",context)
        if password=='':
            context = {"pwinfo":"密码为空"}
            return render(request,"user/login.html",context)
        uob = BlogUser.objects.get(name=name)
        if uob.password == password:
            request.session['bloguser'] = uob.toDict() 
            return redirect(reverse('article_index'))
        else:
            context = {"pwinfo":"密码错误"}
            return render(request,"user/login.html",context)       
    else:
        return HttpResponse("uss")

def logout(request):
    del request.session['bloguser']
    return redirect(reverse('article_index'))

def register(request):
    return render(request,"user/register.html")


def doregister(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if name=='':
            context = {"nameinfo":"名称为空"}
            return render(request,"user/register.html",context)
        #检测用户名是否重复
     
        eob = BlogUser.objects.filter(name=name)
        
        if eob.exists() :
            print('have')
            context = {"nameinfo":"用户名存在"}
            return render(request,"user/register.html",context)
        
        if password!=password2:
            context = {"passwordinfo":"密码不一致"}
            return render(request,"user/register.html",context)
        uob = BlogUser()
        uob.name = name
        uob.password = password2
        uob.save()
        request.session['bloguser'] = uob.toDict()
        return redirect(reverse('article_index'))
    else:
        return HttpResponse("uss")
