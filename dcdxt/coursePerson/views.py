from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
# /coursePerson/index
from majorPerson.models import CourseMark,Teach,Staff,MajorClass,SupportMatrix,Course,Feedback



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
    #print(data)
    return HttpResponse(json_data)


def get_examine(request):
    import json
    info = json.loads(request.POST['info'])
    majorClassNumber = info['classNumber']
    courseNumber = info['courseNumber']
    print(info)

    #找到这门课对应的所有指标点
    supportMatrix = SupportMatrix.objects.filter(course__courseNumber=courseNumber)
    points_related_to_this_course = []
    for item in supportMatrix:
        point = item.point.number
        points_related_to_this_course.append(point)
    print(points_related_to_this_course)

    data_of_inner = []
    for point in points_related_to_this_course:
        temp = CourseMark.objects.filter(course__courseNumber=courseNumber,student__majorClass__classNumber=majorClassNumber,point__number=point)
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

        data_for_this_point = {
            "point":point,
            "level_1": level_1,
            "level_2": level_2,
            "level_3": level_3,
            "level_4": level_4,
            "max_value": max_value,
            "min_value": min_value,
            "avg_value": avg_value
        }
        data_of_inner.append(data_for_this_point)
    teach = Teach.objects.filter(course__courseNumber=courseNumber,majorClass__classNumber=majorClassNumber)
    status = teach[0].status

    data = {
        "status": status,
        "data":data_of_inner
    }
    print(data)
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

def feedback(request):
    import json
    info = json.loads(request.POST['info'])
    majorClassNumber = info["classNumber"]
    courseNumber = info["courseNumber"]
    feedback_content = info["feedback"]
    teacherNumber = request.session['number']

    print(teacherNumber)
    print(info)
    #Look up course
    course = Course.objects.filter(courseNumber=courseNumber)
    #Look up majorClass
    majorClass = MajorClass.objects.filter(classNumber=majorClassNumber)
    #Look up teacher
    teacher = Staff.objects.filter(number=teacherNumber)
    #Look up coursePerson
    print(course)
    coursePerson = course[0].coursePerson

    #New feedback object
    temp = Feedback.objects.create(course=course[0],teacher=teacher[0],majorClass=majorClass[0],coursePerson=coursePerson,reason=feedback_content)
    print(temp)
    temp.save()
    return HttpResponse("OK")
