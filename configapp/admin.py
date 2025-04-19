from django.contrib import admin

from .models import Teacher, Departments, Course, User, Student, GroupStudent
# Register your models here.
admin.site.register([Teacher,Departments,Course,User,Student,GroupStudent])