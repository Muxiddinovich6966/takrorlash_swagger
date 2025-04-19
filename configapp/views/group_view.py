from rest_framework import viewsets
from ..models import GroupStudent
from ..serializers import GroupStudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = GroupStudent.objects.all()
    serializer_class = GroupStudentSerializer