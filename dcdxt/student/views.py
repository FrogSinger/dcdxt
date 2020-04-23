from django.shortcuts import render
from majorPerson.models import *
from django.http import HttpResponse
import json
# /student/index
def index(request):
    return render(request,'student/index.html')

def calculate_point_mark(request):
    studentNumber = request.session['number']
    print(studentNumber)

    result = {}
    mark_on_courses = []
    # Get list of GraduationReqPoints
    points = GraduationReqPoint.objects.all()
    points_list = []
    for point in points:
        number = point.number
        points_list.append(number)
        result[number]=[]
    #print(result)

    #Get the list of courses
    courses = Course.objects.all()
    courses_list = []

    # 对于每个课程，获取它的指标点及评价值
    for course in courses:
        #Coure number
        courseNumber = course.courseNumber
        #Get courses' related points from SupportMatrix
        items = SupportMatrix.objects.filter(course__courseNumber=courseNumber)
        points_list = []
        pointNumber_dict = {} #这门课支撑的指标点列表及其权重
        for item in items:
            pointNumber = item.point.number
            weight = item.weight
            points_list.append(pointNumber)
            pointNumber_dict[pointNumber] = weight #For example:{'1-1': 0.2, '2-1': 0.25}
        #print(pointNumber_dict)

        #Get marks on this course of this student
        #该学生所有的课程
        items = CourseMark.objects.filter(student__number=studentNumber,course__courseNumber=courseNumber)
        mark_dict ={} #该学生在这门课上获得的指标点评价
        #print(items)
        if(len(items)!=0):
            for item in items:
                pointNumber = item.point.number
                mark = item.mark
                mark_dict[pointNumber]=mark
        else:
            continue
        #print(mark_dict) #{'1-1': 0.9, '2-1': 0.7}
        #print(points_list) #{'1-1': 0.2, '2-1': 0.25}

        #计算该学生每个指标点的达成度
        course = Course.objects.filter(courseNumber=courseNumber)
        course = course[0]
        mark_on_this_course = {
            "courseNumber":courseNumber,
            "courseName":course.name,
            "marks":[]
        }
        for point in points_list:
            value = pointNumber_dict[point]*mark_dict[point]
            result[point].append(value)
            temp = {
                point:value
            }
            mark_on_this_course["marks"].append(temp)
        #print(mark_on_this_course)
        mark_on_courses.append(mark_on_this_course)

    for key in result:
        result[key] = sum(result[key])

    #计算每个毕业要求上的达成度

    #Get list of GraduationReq
    graduationReqs = GraduationReq.objects.all()

    #毕业要求的列表
    graduationReqs_list = []
    for graduationReq in graduationReqs:
        graduationReqs_list.append(graduationReq.number)
    print(graduationReqs_list)

    #毕业要求极其对应的指标点
    points_dict = {}
    for graduationReq in graduationReqs_list:
        graduationReqPoints = GraduationReqPoint.objects.filter(GraduationReq__number=graduationReq)
        points_list = []
        for graduationReqPoint in graduationReqPoints:
            points_list.append(graduationReqPoint.number)
        points_dict[graduationReq] = points_list

    print(points_dict)

    #每个毕业要求的达成度
    total_dict = {}
    for key in points_dict:
        mark_list = []
        for i in points_dict[key]:
            mark_list.append(result[i])
        total_dict[key] = min(mark_list)

    print(total_dict)

    #个人总体达成度
    total_list = []
    for key in total_dict:
        total_list.append(total_dict[key])
    total = min(total_list)
    print(total)

    #对于每个指标点，获取它支撑的课程及其评价值
    mark_on_points = {}
    for point in points_list:
        courses = SupportMatrix.objects.filter(point__number=point)
        temp_list = []
        for course in courses:
            courseNumber = course.course.courseNumber
            temp = CourseMark.objects.filter(course__courseNumber=courseNumber,point__number=point,student__number=studentNumber)
            if(len(temp)!=1):
                mark = 0
            else:
                mark = temp[0].mark
            weight = course.weight
            courseName = course.course.name
            temp_dict = {
                "courseName":courseName,
                "weight":weight,
                "mark":mark
            }
            temp_list.append(temp_dict)

        mark_on_points[point] = temp_list
    #print(mark_on_points)


    data = {
        "total":total,
        "total_on_points":total_dict,
        "graduationReqs":points_dict,
        "marks_result":result,
        "mark_on_courses":mark_on_courses,
        "mark_on_points":mark_on_points
    }
    data = json.dumps(data, ensure_ascii=False)
    print(data)
    return HttpResponse(data)