# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(UserInfo)
admin.site.register(GameInfo)
admin.site.register(GameMessage)
admin.site.register(UserHomeMessage)
admin.site.register(OnlineUserList)
