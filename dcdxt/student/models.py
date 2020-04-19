from django.db import models

# Create your models here.
# class Student(models.Model,majorPerson.models.Person):
#     #name = models.CharField(verbose_name='姓名',max_length=100,null=False)
#     #sex = models.CharField(verbose_name='性别',max_length = 10,null=False)
#
#     reachingDegree = models.FloatField(verbose_name='最终达成度',null=True)
#
#     #Foreing key
#     college = models.ForeignKey('majorPerson.College',on_delete=models.SET_NULL,null=True)
#     major = models.ForeignKey('majorPerson.Major',on_delete=models.SET_NULL,null=True)
#     majorClass = models.ForeignKey('majorPerson.MajorClass',on_delete=models.SET_NULL,null=True)
#     instructor = models.ForeignKey('majorPerson.Staff', on_delete=models.SET_NULL,null=True)
#
#
#     def __str__(self):
#         return self.number