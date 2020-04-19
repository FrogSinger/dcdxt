from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
# /coursePerson/index
from majorPerson.models import CourseMark


def index(request):
    return render(request,'coursePerson/index.html')

def get_examine(request):
    grade = "2017"
    majorClassNumber = "201704"
    courseNumber = "140011"

    temp = CourseMark.objects.filter(course__courseNumber=courseNumber,student__majorClass__classNumber=majorClassNumber,student__grade=grade)
    print(temp)
    for item in temp:
        print(item.point.number)

    return render(request, 'coursePerson/course_value.html')