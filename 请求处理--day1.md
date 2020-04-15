####一，用户请求
- 请求类型
	* get
	  - 1，不带参数
	  - 2，带参数
	  ```
	  	  A,位置参数
	  	  B,关键字参数
		     C,?问号
	  	  ```
	* post
	  通常都带参数
- 请求格式
	* path('hello',helloe.index)
	* re_path('hell/(?P<year>[0-9]{4}',hello.index)
	
####二，请求处理
- 带参数get
  -  ？（问号）参数 # http://192.168.1.9/hello/?year=2012&month=12
  	*  urls.py
```
    path('', views.index, name='index'),   
```

	* views.py
```
	from django.http import HttpResponse
	# Create your views here.
	def index(request):
    # 设置默认值的⽅式获取数据更优雅
   	 year = request.GET.get("year", "2019")
    # 直接获取数据，没有传会报错，不建议
    	month = request.GET.get("month", "2")
    	return HttpResponse("year is %s,month is %s" % (year, month))
```
  - 位置参数 http://192.168.1.9/hello/2018/12
  	*  urls.py
```	
	#方法1
	re_path('([0-9]{4})/([0-9]{2})/', views.index, name='index'),
	#方法2 通过正则匹配捕获参数，并通过关键词参数格式传入
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.index,name='index')
```

	* views.py
```
	from django.http import HttpResponse
	#方法1 位置为准
	def index(request,year,month):
   		return HttpResponse("year is %s,month is %s" % (year, month))
    #方法2 可以传递多个，但是只取需要的
	def index(request, **kwargs):
    	 print(kwargs)
    	 year = kwargs.get('year', 2018)
    	 month = kwargs.get('month', 7)
   	  return HttpResponse("year is %s,month is %s" % (year, month))
```
- post请求(hello)
   curl -X POST http://192.168.1.9/hello/ -d 'year=2019&month=09'

	*  urls.py  
```	
	 path('', views.index, name='index'),
```
	* views.py
```
print(request.META['REMOTE_ADDR'])
    #print(request.GET)
    data = request.GET
    year = data.get("year", "2019")
    month = data.get("month", "10")
    if request.method == "POST":
        print(request.method)  # POST
        #print(request.body)  # b'year=2019&month=06'
        print(QueryDict(request.body).dict())
        print(request.POST)  #
        request.POST.getlist('id')
        data = request.POST
        year = data.get("year", "2018")
        month = data.get("month", "07")
    return HttpResponse("year is %s,month is %s" % (year, month))
```