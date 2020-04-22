from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from . import views
app_name = 'hello'
urlpatterns = [
 #path('index.html', views.index, name='index'),
 path('useradd.html',views.useradd,name='useradd'),
 path('userupdate.html', views.userupdate, name='userupdate'),


]
# urlpatterns = [
#     # 2.1: 普通传参url基本和⽆参数⼀样
#     path('', views.index, name='index'),
#     # you can also use regular expressions. To do so, use re_path()instead of path().正则⽤re_path
#     # URL中每个位置数值和view中定义的参数顺序⼀⼀对应（代码可读性不好，不推荐）
#     # 2.2：位置匹配
#     #re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index'),
#     # 2.3：关键字匹配(最优雅) (?<参数名>参数类型)??视图中直接通过参数名获取值（最常⽤）
#
# ]
