# _*_ coding: utf-8 _*_

from .models import Course, Lesson, Video, CourseResource
import xadmin


class CourseAdmin(object):
    list_display = ['name', 'description', 'detail', 'degree', 'student', 'fav_nums', 'image', 'click', 'add_time']
    search_fields = ['name', 'description', 'detail', 'degree', 'student', 'fav_nums', 'image', 'click']
    list_filter = ['name', 'description', 'detail', 'degree', 'student', 'fav_nums', 'image', 'click']


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson__name', 'name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course', 'name']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)