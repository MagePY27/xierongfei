from django.shortcuts import render
from django.http import HttpResponse, QueryDict
import time, datetime
from django.contrib import messages
from hello.models import User
from django.shortcuts import reverse
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import CreateView, DetailView, UpdateView, ListView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class UserAddView(SuccessMessageMixin, CreateView):
    model = User
    fields = ('name', 'password', 'sex','age')
    success_message = "%(name)s was created successfully"

    def get_success_url(self):
        print(self.request.POST)
        if '_addanother' in self.request.POST:
            return reverse('hello:useradd')
        return reverse('hello:userlist')


class UserDetailView(SuccessMessageMixin, DetailView):
    template_name = "hello/user_detail.html"
    # 同价 object = User.objects.get(pk=pk)
    model = User
    # 自定义传给前端模板渲染的变量，默认object
    context_object_name = "user"


class UserDelView(SuccessMessageMixin, DeleteView):
    """
    删除用户
    """
    # 默认模版 hello/user_confirm_delete.html #
    template_name = 'hello/user_confirm_delete.html'
    model = User

    def get_success_url(self):
        return reverse('hello:userlist')


class UserListView(ListView):
    """
    用户列表，最经典的用法，列表+搜索+上下文
     """
    template_name = "hello/user_list.html"
    model = User
    # object_list = User.objects.all() model = User
    # 自定义传给前端模板渲染的变量，默认object_list
    context_object_name = "users"
    keyword = ""

    # 数据过滤
    def get_queryset(self):
        queryset = super(UserListView, self).get_queryset()
        self.keyword = self.request.GET.get("keyword", "")
        if self.keyword:
            queryset = queryset.filter(name=self.keyword)
            #queryset = queryset.filter(name__icontains=self.keyword)

        return queryset

    # 需要传给前端的数据大字典
    # def get_context_data(self, **kwargs):
    #     context = super(UserListView, self).get_context_data(**kwargs)
    #     context['keyword'] = self.keyword
    #     return context


class UserModifyView(SuccessMessageMixin, UpdateView):
    """
    更新用户
    """
    template_name = "hello/user_edit.html"
    model = User
    fields = ('name', 'password', 'sex','age')
    success_message = "%(name)s was update successfully"

    def get_success_url(self):
        if '_continue' in self.request.POST:
            return reverse('hello:usermodify', kwargs={'pk': self.object.pk})
        return reverse('hello:userlist')

# # 添加用户
# def useradd(request):
#     messages = {}
#     if request.method == 'GET':
#         return render(request, 'hello/useradd.html')
#     else:
#         user = request.POST.get('user')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         sex = request.POST.get('gender')
#         age = request.POST.get('age')
#         # 两次密码输入校验
#         if password != password2:
#             messages = {"code":1,"error":"两次输入密码不匹配"}
#             return render(request, 'hello/useradd.html',{"msg": messages})
#         try:
#             users = User.objects.get(name=user)
#             messages = {"code": 1, "error": "用户已经存在"}
#             return render(request, 'hello/useradd.html', {"msg": messages})
#         except User.DoesNotExist:
#             data = {'name': user, 'password': password, 'sex': sex, 'age': age}
#             User.objects.create(**data)
#             messages = {"code": 0, "result": "用户添加成功"}
#         return render(request, 'hello/useradd.html',{"msg": messages})
#
#
# def userlist(request):
#     # 默认显示前5条
#     if request.method == 'GET':
#         users = User.objects.filter().values('id','name', 'sex', 'age').order_by('name')[:5]
#         return render(request, 'hello/userlist.html', {"users": users})
#     else:
#         # 根据用户名搜索
#         if 'search' in request.POST:
#             username = request.POST.get('user',"")
#             try:
#                 users = User.objects.get(name=username)
#             except User.DoesNotExist:
#                 messages.error(request, '没有找到用户')
#                 users = list()
#             users = User.objects.filter(name=username)
#             return render(request, 'hello/userlist.html', {"users": users})
#             # return HttpResponse("%s is delete" % (username))
#         # 表单“更新”功能（根据id
#
# def userdel(request,**kwargs):
#     #return HttpResponse("year is %s" % (kwargs))
#     userid = kwargs.get('pk')
#     if request.method == 'POST':
#         User.objects.filter(id=userid).delete()
#         #return HttpResponse("%s is delete" % (userid))
#         messages = {"code": 1, "error": "删除成功"}
#         # #return HttpResponse("data is %s  keyword %s" % (data,kwargs))
#         #users = User.objects.filter().values('name', 'age').order_by('name')[:5]
#         return render(request, 'hello/userdel.html',{"msg": messages})
#     else:
#         users = User.objects.filter(id=userid).values('name')
#         #return HttpResponse("res is %s %s" % (users[0]['name'],users[0]['age']))
#         return render(request, 'hello/userdel.html', {"users": users})
#
# def usermodify(request,**kwargs):
#     #return HttpResponse("year is %s" % (kwargs))
#     userid = kwargs.get('pk')
#     if request.method == 'POST':
#         # return HttpResponse("year is %s" % (request.POST.get('name')))
#         # data=request.POST.dict()
#         #return HttpResponse("data is %s  keyword %s" % (data,kwargs))
#         # user = User()
#         data = {"name": request.POST.get('name'), "age":request.POST.get('age'),
#                 "sex": request.POST.get('gender'), "password": request.POST.get('password')}
#         User.objects.filter(id=userid).update(**data)
#         messages = {"code": 1, "error": "更新成功"}
#         #return HttpResponse("data is %s  keyword %s" % (data,kwargs))
#         #User.objects.filter(id=userid).update(**data)
#         return render(request, 'hello/usermodify.html', {"msg": messages})
#     else:
#         users = User.objects.filter(id=userid).values('id', 'name', 'sex', 'age','password')
#         #return HttpResponse("res is %s %s" % (users[0]['name'],users[0]['age']))
#         return render(request, 'hello/usermodify.html', {"users": users})
