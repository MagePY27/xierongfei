####一，模板基础
- 功能介绍
	将试图返回的数据进行渲染生成页面展示给用户
- 配置说明

  项目工程下建立 templates,该目录按照应用名字建立文件夹并存放对应app的模板
    templates/hell
	* BACKEND 是一个指向实现了Django模板后端API的模板引擎类的带点的Python路径。内置
的有django.template.backends.django.DjangoTemplates 和django.template.backends.jinja2.Jinja2.两个模板差不多
	* DIRS 定义了⼀个⽬录列表，模板引擎按列表顺序搜索这些⽬录以查找模板源⽂件。默认会
先找templates⽬录
	```
	'DIRS': [os.path.join(BASE_DIR, 'templates')],
	```
	* APP_DIRS 告诉模板引擎是否应该进⼊已安装的应⽤中查找模板。每种模板引擎后端都
定义了⼀个惯⽤的名称作为应⽤内部存放模板的子目录名

####二，参数传递
- 变量，字典，列表参数传递

	* views.py
	
```
	def index(request):
    classname = "DevOps"
    books = ['Python', 'Java', 'Django']
    user = {'name': 'kk', 'age': 18}
    userlist = [{'name': 'kk', 'age': 18}, {'name': 'rock', 'age': 19},
                {'name': 'mage', 'age': 20}]
    return render(request, 'hello/index.html', \
                  {'classname': classname, "books": books,"user": user, "userlist": userlist})

```
	* hello/index.html
	
```
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<head> <meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>DevOps</title>
<ul>
    <li> {{books.0}} </li>
    <li> {{books.1}} </li>
    <li> {{books.2}} </li>
</ul>
<div color = blue>hello my name is {{ user.name }} </br>
 my age is {{ user.age }}
</div>
{# if标签使⽤，判断user是否存在 #}
{% if user %}
   <p> name:{{ user.name }} </p>
{%else%}
   ⽤户不存在
{% endif %}
{# for循环标签，渲染books列表 #}
    {% for book in books %}
    <li>{{ book }}</li>
    {% endfor %}
{# for循环输出列表嵌套字典数据 #}
<table border="1">
  <tr>
    <th>用户名</th>
    <th>年龄</th>
  </tr>
    {% for user in userlist %}
  <tr>
    <td>{{ user.name }}</td>
    <td>{{ user.age }}</td>
  </tr>
    {% endfor %}
</table>

</body>
</html>
````
####三，页面继承
- 模板页面（包含所有页面共有信息）
	block 部分为子页面变化内容
	```
{% block content %}
 {% endblock %}
    ```
- 子页面
	继承基础页面内容，并添加自定义内容，也可重新父页面
    
	```
#导入模板
{% extends "base.html" %}
#block为子页面内容
{% block content %}
<ul>
    <li> {{books.0}} </li>
    <li> {{books.1}} </li>
    <li> {{books.2}} </li>
</ul>
{% endblock %}
    ```

####四，过滤器
- 自带过滤器
- 自定义过滤器
