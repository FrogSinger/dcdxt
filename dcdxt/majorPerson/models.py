from django.db import models

# Create your models here.
class College(models.Model):
    collegeNumber = models.CharField(verbose_name='学院编号',max_length=10,null=False)
    name = models.CharField(verbose_name='学院名称',max_length=200,null=False)

    def __str__(self):
        return self.name


class Major(models.Model):
    majorNumber = models.CharField(verbose_name='专业编号',max_length=20,null=False)
    name = models.CharField(verbose_name='专业名称', max_length=200, null=False)

    def __str__(self):
        return self.name

class MajorClass(models.Model):
    classNumber = models.CharField(verbose_name='班级编号',max_length=20,null=False)
    name = models.CharField(verbose_name='班级名称', max_length=200, null=False)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(verbose_name='姓名', max_length=100, null=False)
    sex = models.CharField(verbose_name='性别', max_length=10, null=False)
    number = models.CharField(verbose_name='ID', max_length=20, null=False)
    grade = models.CharField(verbose_name='年级',max_length=5,null=True)

    def __str__(self):
        return self.name

class Staff(Person):
    #Foreign key
    college = models.ForeignKey('College', on_delete=models.SET_NULL,null=True)
    major = models.ForeignKey('Major', on_delete=models.SET_NULL,null=True)

class User(models.Model):
    user = models.ForeignKey('Person',on_delete=models.SET_NULL,null=True)
    type = models.CharField(verbose_name='用户类别',max_length=100,null=False)
    password = models.CharField(verbose_name='密码',max_length=64,default='12345678',null=False)
    status = models.BooleanField(verbose_name='状态',default=True,null=False)

class Course(models.Model):
    courseNumber = models.CharField(verbose_name='课程ID',max_length=20,null=False)
    name = models.CharField(verbose_name='课程名称',max_length=100,null=False)
    coursePerson = models.ForeignKey('Staff',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.name

class GraduationReq(models.Model):
    number = models.CharField(verbose_name='毕业要求编号',max_length=5,null=False)
    content = models.CharField(verbose_name='毕业要求内容',max_length=1000,null=True)

    def __str__(self):
        return self.number

class GraduationReqPoint(models.Model):
    number = models.CharField(verbose_name='指标点编号', max_length=10,null=False)#Such as 1-1/1-2/2-1
    content = models.CharField(verbose_name='指标点内容', max_length=1000, null=True)
    GraduationReq = models.ForeignKey('GraduationReq',on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.number

class SupportMatrix(models.Model):
    course = models.ForeignKey('Course',on_delete=models.SET_NULL, null=True)
    point = models.ForeignKey('GraduationReqPoint',on_delete=models.SET_NULL, null=True)
    weight = models.FloatField(verbose_name='权重', null=False)

class CourseMark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    point = models.ForeignKey('GraduationReqPoint', on_delete=models.SET_NULL, null=True)
    mark = models.FloatField(verbose_name='评价值', null=True)

class PointMark(models.Model):
    student = models.ForeignKey('Student',on_delete=models.SET_NULL, null=True)
    point = models.ForeignKey('GraduationReqPoint',on_delete=models.SET_NULL, null=True)
    mark = models.FloatField(verbose_name='达成度', null=True)

class GraduationReqMark(models.Model):
    student = models.ForeignKey('Student', on_delete=models.SET_NULL, null=True)
    GraduationReq = models.ForeignKey('GraduationReq', on_delete=models.SET_NULL, null=True)
    mark = models.FloatField(verbose_name='达成度', null=True)

class Teach(models.Model):
    course = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey('Staff', on_delete=models.SET_NULL, null=True)
    majorClass = models.ForeignKey('MajorClass', on_delete=models.SET_NULL, null=True)
    #0代表未审核，1代表审核通过，2代表未审核通过
    status = models.IntegerField(verbose_name='审核状态',default=0,null=False)

class Student(Person):
    #name = models.CharField(verbose_name='姓名',max_length=100,null=False)
    #sex = models.CharField(verbose_name='性别',max_length = 10,null=False)

    reachingDegree = models.FloatField(verbose_name='最终达成度',null=True)

    #Foreing key
    college = models.ForeignKey('College',on_delete=models.SET_NULL,null=True)
    major = models.ForeignKey('Major',on_delete=models.SET_NULL,null=True)
    majorClass = models.ForeignKey('MajorClass',on_delete=models.SET_NULL,null=True)
    instructor = models.ForeignKey('Staff', on_delete=models.SET_NULL,null=True)


    def __str__(self):
        return self.number