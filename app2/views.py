# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
# Create your views here.
import fake
from .models import *
def login(req):
    return render(req,template_name='login.html')

def userHome(req):
    if req.POST:
        username=req.POST['username']
        password=req.POST['password']
        print(username,password)
        try:
            user=UserInfo.objects.get(username=username)
            if user.password==password:
                context = {'userInfo':user}
                req.session['login']=True
                req.session['username']=username
                return render(req, template_name='userHome.html',context=context)
        except :
            return render(req,template_name='login.html',context={'error':'用户名或错误'})
    else:
        return render(req,template_name='login.html',context={'error':'请登录'})

    return render(req,template_name='login.html',context={'error':'或密码错误'})

def game(req):
    if req.session.has_key('login'):
        print('登录用户正在邀请xxx')
    return render(req,template_name='game.html')

def onlineUserList(req):
    return JsonResponse(fake.fakeUserlist(req))

def checkInvitation(req):
    return JsonResponse(fake.fakeInvitation(req))









