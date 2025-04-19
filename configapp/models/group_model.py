from .auth_user import *
from .teacher_model import *


class  GroupStudent(BaseModel):
    title = models.CharField(max_length=40,null=True, unique=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher, related_name='teacher_get')