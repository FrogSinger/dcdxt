from django.db import models
from majorPerson.models import College,Major,MajorClass

# Create your models here.
class Student(models.Model):
    studentNumber = models.IntegerField(verbose_name='学号',null=False)
    name = models.CharField(verbose_name='姓名',max_length=100,null=False)
    sex = models.CharField(verbose_name='性别',max_length = 10,null=False)
    grade = models.IntegerField(verbose_name='年级', max_length=10, null=False)

    reachingDegree = models.FloatField(verbose_name='最终达成度',null=True)

    #Foreing key
    college = models.ForeignKey('majorPerson.College',on_delete=models.SET_NULL)
    major = models.ForeignKey('majorPerson.Major',on_delete=models.SET_NULL)
    majorClass = models.ForeignKey('majorPerson.MajorClass',on_delete=models.SET_NULL)


    def __str__(self):
        return self.studentNumber

    class Meta:
        db_table = 'student'