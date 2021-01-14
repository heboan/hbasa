from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    real_name = models.CharField(max_length=20, default='', verbose_name='姓名')
    gender = models.CharField(max_length=1, choices=(('m', '男'),('f', '女')), default='m', verbose_name='性别')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100, verbose_name='头像')
    title = models.CharField(max_length=20, default='', verbose_name='职位')
    department= models.CharField(max_length=100, default='', verbose_name='部门')

    def __self__(self):
        return self.username