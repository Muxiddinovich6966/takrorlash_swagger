
from rest_framework import serializers
from ..models import teacher_model, group_model, GroupStudent
from .teacher_serializer import *


class GroupStudentSerializer(serializers.ModelSerializer):

      teacher = TeacherSerializer(read_only=Teacher,many=True)

      class Meta:
          model = GroupStudent
          fields = '__all__'


