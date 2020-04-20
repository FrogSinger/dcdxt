from django.shortcuts import render
from majorPerson.models import *
from django.http import HttpResponse
from django.db.models import Q

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
    return render(request,'teacher/import_value.html',{'data':data})

# /teacher/import_course_data
def import_course_data(request):
    json_text = {"courseName":"微积分","points":["1-1","2-1"],"value":[{"studentNumber":"2017115171","point":[0.7,0.8]},{"studentNumber":"2017115191","point":[1,0.9]},{"studentNumber":"2017115182","point":[0.65,0.75]}]}
    courseName = json_text["courseName"]
    #classNumber = json_text["classNumber"]
    points = json_text["points"]
    value = json_text["value"]

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
