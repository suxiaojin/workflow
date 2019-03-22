# _*_ coding:utf-8 _*_
from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserProfile(AbstractUser):
    """
    用户信息表
    """
    mobile=models.CharField(max_length=11,verbose_name=u'手机号码',default='')
    image=models.ImageField(upload_to='images/%Y/%m',default=u'images/default.jpg',max_length=100,verbose_name=u'头像')
    dept=models.CharField(max_length=20,verbose_name=u'部门',default='')

    class Meta:
        verbose_name='用户信息'
        verbose_name_plural=verbose_name

    def __str__(self):
        return "%s" %self.username

class EmailVerifyRecord(models.Model):
    code=models.CharField(max_length=20,verbose_name=u"验证码")
    email=models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type=models.CharField(verbose_name=u"验证码类型",choices=(('register',u'注册'),('forget',u'找回密码'),('update_email',u'修改邮箱')),max_length=30)
    send_time=models.DateField(verbose_name=u'发送时间',default=datetime.now)

    class Meta:
        verbose_name=u'邮箱验证码'
        verbose_name_plural=verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.code,self.email)

