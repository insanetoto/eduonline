# _*_ coding: utf-8 _*_
from .models import UserAsk, CourseComment, UserFavorate, UserMessage, UserCourse
import xadmin


class UserAskAdmin(object):
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    search_fields = ['name', 'mobile', 'course_name']
    list_filter = ['name', 'mobile', 'course_name']


class CourseCommentAdmin(object):
    list_display = ['user', 'course', 'comments', 'add_time']
    search_fields = ['user', 'course', 'comments']
    list_filter = ['user__nike_name', 'course', 'comments']


class UserFavorateAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user__nike_name', 'fav_id', 'fav_type']
    list_filter = ['user__nike_name', 'fav_id', 'fav_type']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read']
    list_filter = ['user', 'message', 'has_read']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user__nike_name', 'course']
    list_filter = ['user__nike_name', 'course']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorate, UserFavorateAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)


