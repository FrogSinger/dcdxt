from django.shortcuts import render
from majorPerson.models import *
from django.http import HttpResponse
from django.http import FileResponse
from django.shortcuts import redirect
import json

# /teacher/index
def index(request):
    return render(request, 'teacher/index.html')

def login(request):
    # judge login status
    if request.session.has_key('userType'):
        userType = request.session['userType']
        if request.session.has_key('islogin'):
            if (userType == "学生"):
                return render(request, 'student/index.html')
            if (userType == "导员"):
                return render(request, 'instructor/index.html')
            if (userType == "教师"):
                return render(request, 'teacher/import_value.html')
            if (userType == "专业负责人"):
                return render(request, 'majorPerson/import_supportMatrix.html')
            if (userType == "课程负责人"):
                return render(request, 'coursePerson/course_value.html')
    else:
        return render(request, 'login.html')

# /loginHandle
def loginHandle(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username,password)
    # remember login status
    request.session['islogin'] = True
    #look up in database
    islogin = User.objects.filter(user__number=username,password=password)
    userType = islogin[0].type
    #Save user type
    request.session['userType'] = userType
    if (len(islogin)>=1):
        if (userType == "学生"):
            return render(request, 'student/index.html')
        if (userType == "导员"):
            return render(request, 'instructor/index.html')
        if (userType == "教师"):
            return render(request, 'teacher/import_value.html')
        if (userType == "专业负责人"):
            return render(request, 'majorPerson/import_supportMatrix.html')
        if (userType == "课程负责人"):
            return render(request, 'coursePerson/course_value.html')
        #return JsonResponse({'res': 1})
    else:
        return HttpResponse("Login error")

#exit
def exit(request):
    #request.session['islogin'] = False
    request.session.flush()
    return render(request, 'login.html')

# /teacher/import_course
def import_course(request):
    return render(request, 'teacher/import_value.html')

# /teacher/get_course_data
def get_course_data(request):
    number = "127239240" # 登录页面从前端传的工号
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

    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data)

# /teacher/import_course_data
def import_course_data(request):
    info = json.loads(request.POST['info'])
    courseNumber = info["courseNumber"]
    #classNumber = info["classNumber"]
    points = info["points"]
    value = info["value"]

    course = Course.objects.get(courseNumber=courseNumber)

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

def get_value_data(request):
    info = json.loads(request.POST['info'])
    courseNumber = info["courseNumber"]
    classNumber = info["classNumber"]

    teach = Teach.objects.filter(course__courseNumber=courseNumber, majorClass__classNumber=classNumber)
    status = teach[0].status

    items = CourseMark.objects.filter(course__courseNumber=courseNumber,student__majorClass__classNumber=classNumber)
    data = []
    for item in items:
        point = item.point.number
        studentNumber = item.student.number
        name = item.student.name
        mark = item.mark
        temp = {
            "point":point,
            "studentNumber":studentNumber,
            "name":name,
            "mark":mark
        }
        data.append(temp)
    data = {
        "status":status,
        "data":data
    }
    data = json.dumps(data, ensure_ascii=False)
    #print(data)
    return HttpResponse(data)

def download_course_template(request):
    file=open('static/files/template_course.xlsx','rb')
    response =FileResponse(file)
    response['Content-Type']='application/octet-stream'
    response['Content-Disposition']='attachment;filename="template_course.xlsx"'
    return response