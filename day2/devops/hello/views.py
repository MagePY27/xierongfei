from django.shortcuts import render
from django.http import HttpResponse, QueryDict
import time,datetime
from django.contrib import messages
from hello.models import User


# 添加用户
def useradd(request):
    if request.method == 'GET':
        return render(request, 'hello/useradd.html')
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        sex = request.POST.get('gender')
        age = request.POST.get('age')
        #两次密码输入校验
        if password != password2:
            messages.error(request, '两次输入密码不匹配')
            return render(request, 'hello/useradd.html')
        try:
            users = User.objects.get(name=user)
            messages.error(request, '用户已经存在')
        except User.DoesNotExist:
            data = {'name': user, 'password': password, 'sex': sex, 'age':age}
            User.objects.create(**data)
            messages.error(request, '用户添加成功')
        return render(request, 'hello/useradd.html')

def userupdate(request):
    # 默认显示前5条
    if request.method == 'GET':
        users = User.objects.filter().values('name', 'sex','age').order_by('name')[:5]
        return render(request, 'hello/userupdate.html',{"users": users})
    else:
        #根据用户名搜索
        if 'search' in request.POST:
            username = request.POST.get('user')
            try:
                users = User.objects.get(name=username)
            except User.DoesNotExist:
                messages.error(request, '没有找到用户')
                users = list()
            users = User.objects.filter(name=username)
            return render(request, 'hello/userupdate.html',{"users": users})
            #return HttpResponse("%s is delete" % (username))
        #表单“更新”功能（根据id
        if 'update' in request.POST:
            username = request.POST.get('user')
            gender = request.POST.get('gender')
            age = request.POST.get('age')
            data = {"sex": gender, "name": username,"age":age}
            #return HttpResponse("year is %s" % (request.body))
            User.objects.filter(name=username).update(**data)
            messages.error(request, '更新成功')
            users = User.objects.filter().values('name', 'sex', 'age').order_by('name')[:5]
            return render(request, 'hello/userupdate.html', {"users": users})

        if 'delete' in request.POST:
            username = request.POST.get('user')
            user = User.objects.get(name=username)
            user.delete()
            messages.error(request, '删除成功')
            users = User.objects.filter().values('name', 'age').order_by('name')[:5]
            return render(request, 'hello/userupdate.html', {"users": users})




