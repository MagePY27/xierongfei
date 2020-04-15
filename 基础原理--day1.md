####一，层级关系
- 工程（project)
	一个共工程里包含多个功能模块，比如运维平台
- 模块（app)
	实现某些功能

####二，项目流程
- 创建model 设计表
- 导入表结构  python migrate xxxx #app name
- 创建路由 
	指明用户请求由那个框架进行逻辑处理
- 处理逻辑
####三，MVT架构
- models
	存放用户数据
- views
	请求处理，数据加工
- template
	对处理后的数据进行渲染生成html文件，返回给用户
####四，第一个项目
- 创建项目应用
```
	  django-admin startproject devops
      cd devops 
      django-admin startapp devops
```
- 迁移
  导入模板数据库，python migrate xxxx #app name
- 基础配置（devops/settings.py)
 * 配置项目下的ALLOWED_HOSTS = ['*']
 * INSTALLED_APPS设置。 它保存这个Django实例中激活的所有的Django应用的名字。
 * 数据库
 ```
	 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'USER': 'test',
        'PASSWORD': '123456',
        'HOST': '192.168.1.240',
        'PORT': '3306',
       }
  }
```
* 时区


https://docs.djangoproject.com/en/1.8/
----urls定义-----
	每个app单独配置urls.py;工程做映射
	----app01/urls.py----
	from django.conf.urls import url
	from . import views
	urlpatterns = [
        url(r'^$', views.current_datetime),
		]
	----app01/views.py------------
	from django.shortcuts import render,render_to_response 
	from django.http import HttpResponse
	from django.template import RequestContext
	import datetime
	def current_datetime(request):
		# View code here...
		now = datetime.datetime.now()
		return render(request, 'index.html', {'time':now})
		#使用app01模板
		#return render(request, 'app01/index.html', {'time':now})
	---- ./myproject/urls.py 主url配置----
		urlpatterns = [
			url(r'^admin/', admin.site.urls),
			url(r'^app01/', include('app01.urls')),
		]
----template设置----
    公用模板 ./templates
	应用模板 app01/templates/app01/index.html
	---- myproject/setting.py
     TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
	............
    INSTALLED_APPS = [
       'app01', ]  #定义应用
	 
	----app01/templates/app01/index.html
	#http://192.168.1.253:8200/static/app01/images/test.png
	{% load staticfiles %}
	<html>
		<body>
			<h1>--------app01------------{{time}}----------------------</h1>
			<img src="{% static "app01/images/test.png" %}" alt="My image"/>
		</body>
	<html>
	
	
