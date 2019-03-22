# -*- coding: utf-8 -*-
__author__ = 'suxiaojin'
__date__ = '2019/3/15 0015 上午 11:10'
import xadmin
from .models import UserProfile,EmailVerifyRecord
from xadmin import views

class UserProfileAdmin(object):
    list_display=['username','email','mobile','dept','image']
    search_fields=['username','dept','mobile']
    list_filter= ['username', 'dept', 'mobile']

class EmailVerifyRecordAdmin(object):
    list_display=['email','code','send_type','send_time']
    search_fields=['email','send_time']
    list_filter= ['email']



class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True

class GlobalSettings(object):
    site_title="系统运维平台"
    site_footer="大数据中心"
    menu_style="accordion"

xadmin.site.unregister(UserProfile)
xadmin.site.register(UserProfile,UserProfileAdmin)

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)