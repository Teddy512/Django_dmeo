from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb import models

# Create your views here.

user_list=[
    {"user":"jack","pwd":"abc"},
    {"user":"tom","pwd":"abc"},
]


def index(request):

    # return HttpResponse("hello world!")  #不能直接返回字符串，要封装后返回
    if request.method=="POST":
        username=request.POST.get("username",None)
        password=request.POST.get("password0",None)
        # print (username,password)
        # temp={"user":username,"pwd":password}
        # user_list.append(temp)
        #添加到数据库里面
        models.UserInfo.objects.create(user=username,pwd=password)
    #从数据库里识别数据-------从数据库力面读取所有行
    user_list=models.UserInfo.objects.all()

    return render(request,"index.html",{"data":user_list})
