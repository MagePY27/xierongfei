####一，开始建模
- 定义
- 日常操作
```
python manage.py makemigrations hello # ⽣成迁移脚本
 python manage.py sqlmigrate hello 0001 # 展示迁移的sql语句
 python manage.py migrate # 执⾏数据库命令
 python manage.py showmigrations # 所有的app及对应的
已经⽣效的migration
 # 将某个app的migration重置，出现冲突时这么⼲，
 python manage.py migrate --fake hello hello
 # 强制执⾏某个版本的迁移脚本
 python manage.py migrate --fake hello
 python manage.py migrate --fake hello 0003
```
####二，增删改查
- console环境启动
```
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devops.settings") 
django.setup()
```
- 增加

```
    from hell.models impor User
	#方法1
    u = User()
    u.name = 'abcde'
    u.password = '123456'
	# u = User(name='abcd',password='123456')
    u.save()
    #方法2（常用)
	data = {'name':'test06','password':'123456'}
	User.objects.create(**data)
```

- 删除
```
 #方法1
 u = User.objects.get(name='kk') # 删除⼀条
 u.delete()
 u.objects.filter(name='k').delete() # 删除匹配的所有
 #方法2
 data = {'name':'kk'}
 u.objects.filter(**data).delete()
 u.objects.all().delete() # 删除所有
```
- 修改
```
# 指定列更新
user.objects.filter(id=52).update(name="cjk",password='123') 
# 不定⻓的更新
data = {'name':'cjk','password':'123456'}
user.objects.filter(id=52).update(**data)
```
- 查询
	* 查询多条数据---返回结果为列表嵌套字典
```
def userlist(request):
    users = User.objects.all()
    for user in users: # 遍历查询的数据
 		print(user.name)
 User.objects.all().values_list('name', 'password') # 返回结果为列表嵌套元组
  User.objects.all().values('name', 'password') # 返回结果为列表嵌套字典
```
	* 条件查询
```
#filter返回多个
User.objects.filter(id=1) 
User.objects.filter(id=1).values() # 查出全部结果以列表嵌套字典形式显示
User.objects.filter(id=1).values('id','name') # 只列出指定的列
#get返回一个
res = User.objects.get(name="cjk"); # 返回⼀个对象，name相当于where条件
res.name # 通过属性获取对应的值
res.password
#等价于
  data = {'name':'cjk'}
  res = User.objects.get(**data); 
  res.name
# 排序倒序
User.objects.all().order_by('name')
User.objects.all().order_by('-name') # 在name 前加⼀个负号，可以实现倒序
```
* raw执⾏原⽣sql
```
from hello.models import User 
res = User.objects.raw('select * from hello_user') 
for user in res: 
```
