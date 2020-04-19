from django.shortcuts import render
from majorPerson.models import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
# /teacher/index
def index(request):
    return render(request,'teacher/index.html')

# /teacher/import_data
def import_course_data(request):
    json_text = {"courseName":"微积分","points":["1-1","2-1"],"value":[{"studentNumber":"2017115171","point":[0.7,0.8]},{"studentNumber":"2017115191","point":[1,0.9]},{"studentNumber":"2017115182","point":[0.65,0.75]}]}
    courseName = json_text["courseName"]
    #classNumber = json_text["classNumber"]
    points = json_text["points"]
    value = json_text["value"]

    course = Course.objects.get(name=courseName)


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
