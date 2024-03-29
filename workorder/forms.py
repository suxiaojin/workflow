# -*- coding: utf-8 -*-
__author__ = 'suxiaojin'
__date__ = '2019/3/19 0019 下午 15:42'
from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username=forms.CharField(required=True)
    password=forms.CharField(required=True,min_length=5)

class RegisterForm(forms.Form):
    email=forms.EmailField(required=True)
    password=forms.CharField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u"验证码错误"})

class ForgetForm(forms.Form):
    email=forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':u"验证码错误"})

class ModifyPwdForm(forms.Form):
    password1=forms.CharField(required=True)
    password2=forms.CharField(required=True)