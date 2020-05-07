from django.shortcuts import render
from django.http import HttpResponse, QueryDict
import time, datetime
from django.contrib import messages
from hello.models import User
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import CreateView, DateDetailView, UpdateView, ListView, DeleteView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # 将数据存⼊到context上下⽂中，给前端渲染
        context = {}
        context['users'] = User.objects.all()
        # context⾥的数据传递到about.html中去渲染
        return context

    def post(self, request):
        data = request.POST.dict()
        print(data)
        User.objects.create(**data)
        users = User.objects.all()
        return render(request, 'index.html', {"users": users})
# class IndexView(View):
#     def get(self, request):
#         users = User.objects.all()
#         return render(request, 'index.html', {"users": users})
#
#     def post(self, request):
#         data = request.POST.dict()
#         print(data)
#         User.objects.create(**data)
#         users = User.objects.all()
#         return render(request, 'index.html', {"users": users})
# class IndexView(View):
#
#     def get(self, request):
#         return HttpResponse("get")
#
#     def put(self, request):
#         return HttpResponse("put")
#
#     def post(self, request):
#         return HttpResponse("post")
#
#     def delete(self, request):
#         return HttpResponse("delete")
