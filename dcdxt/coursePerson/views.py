from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
# /coursePerson/index
from majorPerson.models import CourseMark,Teach,Staff,MajorClass



def index(request):
    return render(request,'coursePerson/index.html')

def course_value(request):
    return render(request, 'coursePerson/course_value.html')

#Init data
def course_examine(request):
    #Information get from cookie
    number="813710901"
    grade="2017"
    #Get list of classes
    coursePerson = Staff.objects.filter(number=number)
    major = coursePerson[0].major
    classes = MajorClass.objects.filter(major=major)
    #Get class list of this coursePerson
    data = []
    class_list = []
    course_list = []
    for item in classes:
        classNumber = item.classNumber
        className = item.name

        #这个班级对应的课程
        teach = Teach.objects.filter(majorClass__classNumber=classNumber,course__coursePerson__number=number)
        course_list_temp = []
        #这个班级的每一门课程
        for temp in teach:
            if(temp.course):
                courseNumber = temp.course.courseNumber
                courseName = temp.course.name
                course_info = {
                    "courseNumber":courseNumber,
                    "courseName":courseName
                }
                course_list_temp.append(course_info)

        data_temp = {
            "classNumber":classNumber,
            "className":className,
            "course_list":course_list_temp
        }
        data.append(data_temp)
    #print(data)
    import json
    json_data = json.dumps(data,ensure_ascii=False)
    print(data)
    return HttpResponse(json_data)


def get_examine(request):
    import json
    info = json.loads(request.POST['info'])
    majorClassNumber = info['classNumber']
    courseNumber = info['courseNumber']
    print(info)

    temp = CourseMark.objects.filter(course__courseNumber=courseNumber,student__majorClass__classNumber=majorClassNumber)
    #print(temp)
    level_1 = 0
    level_2 = 0
    level_3 = 0
    level_4 = 0

    marks = []
    for item in temp:
        if(item.mark>=0.9):
            level_1 = level_1+1
        if (item.mark >= 0.8 and item.mark<0.9):
            level_2 = level_2 + 1
        if (item.mark >= 0.65 and item.mark<0.8):
            level_3 = level_3 + 1
        if (item.mark < 0.65):
            level_4 = level_4 + 1
        marks.append(item.mark)

    max_value = max(marks)
    min_value = min(marks)
    avg_value = sum(marks)/len(marks)

    teach = Teach.objects.filter(course__courseNumber=courseNumber,majorClass__classNumber=majorClassNumber)
    status = teach[0].status

    data = {
        "status": status,
        "level_1":level_1,
        "level_2": level_2,
        "level_3": level_3,
        "level_4":level_4,
        "max_value":max_value,
        "min_value":min_value,
        "avg_value":avg_value
    }
    import json
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data)

#When user click the examine button
def examine(request):
    import json
    info = json.loads(request.POST['info'])
    status = info["status"]
    majorClassNumber = info["classNumber"]
    courseNumber = info["courseNumber"]

    teach = Teach.objects.filter(course__courseNumber=courseNumber, majorClass__classNumber=majorClassNumber)
    print(teach[0].status)
    temp = teach[0]
    temp.status = status
    temp.save()
    if(temp.status==status):
        return HttpResponse("OK")
