
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *
from .views.group_view import GroupViewSet
from .views.student_view import StudentApi
from .views.teacher_view import TeacherViewSet

router = DefaultRouter()
router.register(r'teacher', TeacherViewSet, basename='teacher')
router.register(r'group', GroupViewSet, basename='group')
router.register(r'student', StudentApi, basename='student')

urlpatterns = [

    path('', include(router.urls)),
]