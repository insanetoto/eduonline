# _*_ coding: utf-8 _*_

import xadmin

from .models import EmailVerifyRecord, Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['index', 'title', 'url', 'add_time']
    search_fields = ['index', 'title', 'url']
    list_filter = ['index', 'title', 'url', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)

