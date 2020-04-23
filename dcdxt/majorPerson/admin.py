from django.contrib import admin

# Register your models here.
from majorPerson.models import *
# from student.models import Student
# Register your models here.

class CollegeAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['collegeNumber','name']
    #上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']

class MajorAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['majorNumber','name']
    #上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']

class MajorClassAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['classNumber','name']
    #上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']

class StaffAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name','sex','number','college','major']
    #上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['number']
    search_fields = ['name']

class StudentAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['name','sex','number','college','major','majorClass','instructor','reachingDegree']
    #上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['number']
    search_fields = ['name']

class UserAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['user', 'type', 'password', 'status']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['status']
    search_fields = ['name']

class CourseAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['courseNumber', 'name', 'coursePerson']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['courseNumber']
    search_fields = ['name']

class GraduationReqAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['number']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['number']
    search_fields = ['number']

class GraduationReqPointAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['number','GraduationReq']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['number']
    search_fields = ['number']

class SupportMatrixAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['course','point','weight']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['course']
    search_fields = ['point']

class CourseMarkAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['student','course','point','mark']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['course']
    search_fields = ['point']

class PointMarkAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['student','point','mark']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['point']
    search_fields = ['point']

class GraduationReqMarkAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['student','GraduationReq','mark']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['GraduationReq']
    search_fields = ['GraduationReq']

class TeachAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['course','teacher','majorClass','status']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['course']
    search_fields = ['teacher']

class FeedbackAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['course','teacher','majorClass','coursePerson','examine_time','status']
    # 上面既可以是属性名，也可以是方法名
    actions_on_bottom = True
    list_filter = ['course','teacher']
    search_fields = ['teacher']

admin.site.register(College,CollegeAdmin)
admin.site.register(Major,MajorAdmin)
admin.site.register(MajorClass,MajorClassAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(GraduationReq,GraduationReqAdmin)
admin.site.register(GraduationReqMark,GraduationReqMarkAdmin)
admin.site.register(GraduationReqPoint,GraduationReqPointAdmin)
admin.site.register(SupportMatrix,SupportMatrixAdmin)
admin.site.register(CourseMark,CourseMarkAdmin)
admin.site.register(PointMark,PointMarkAdmin)
admin.site.register(Teach,TeachAdmin)
admin.site.register(Feedback,FeedbackAdmin)

admin.site.site_header="西北大学毕业要求达成度系统管理后台"
