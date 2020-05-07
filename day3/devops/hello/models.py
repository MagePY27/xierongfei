from django.db import models


# Create your models here.

class User(models.Model):
    SEX = (
        (0, '男'),
        (1, '女'),
    )
    name = models.CharField(max_length=20, help_text="用户名")
    password = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    sex = models.IntegerField(choices=SEX, null=True, blank=True)

    # def __str__(self):
    #     return self.name, self.sex
