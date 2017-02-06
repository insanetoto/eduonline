# _*_ coding: utf-8 _*_
from .models import CourseOrg, Teacher, CityDict
import xadmin


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'address', 'city']
    list_filter = ['name', 'desc', 'address', 'city']


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'add_time']
    search_fields = ['name', 'work_years', 'work_company', 'work_position', 'points']
    list_filter = ['org__name', 'name', 'work_years', 'work_company', 'work_position', 'points']


class CityDictAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(CityDict, CityDictAdmin)
