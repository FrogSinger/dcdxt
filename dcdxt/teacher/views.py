from django.shortcuts import render
from majorPerson.models import *
from django.http import HttpResponse
from django.db.models import Q
import json

# Create your views here.

# /login
def login(request):
    return render(request,'login.html')

# /loginHandle
def loginHandle(request):
    return render(request,'teacher/index.html')

# /teacher/import_course
def import_course(request):
    number = "127239240"

    teach = Teach.objects.filter(teacher__number=number)
    data = []
    for item in teach:
        courseNumber = item.course.courseNumber
        courseName = item.course.name
        classNumber = item.majorClass.classNumber
        className = item.majorClass.name
        temp = {
            "courseNumber":courseNumber,
            "courseName":courseName,
            "classNumber":classNumber,
            "className":className
        }
        data.append(temp)
        #print(data)
    return render(request,'teacher/import_value.html',{'data':data})

# /teacher/import_course_data
def import_course_data(request):
    info = json.loads(request.POST['info'])
    courseName = info["courseName"]
    #classNumber = json_text["classNumber"]
    points = info["points"]
    value = info["value"]
    print(info)

    course = Course.objects.get(name=courseName)
    print(course)

    for i in range(len(value)):
        student = Student.objects.get(number=value[i]['studentNumber'])
        for j in range(len(points)):
            point = GraduationReqPoint.objects.get(number=points[j])
            mark = value[i]['point'][j]
            obj = CourseMark.objects.create(student=student,course=course,point=point,mark=mark)
            # delete repeat
            repeat = CourseMark.objects.filter(student=student,course=course,point=point)
            for item in repeat:
                item.delete()
            obj.save()
    return HttpResponse('OK')
