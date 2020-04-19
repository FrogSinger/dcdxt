from django.shortcuts import render
from django.http import HttpResponse
from majorPerson.models import *
import json

# Create your views here.
def index(request):
    return render(request,'majorPerson/index.html')

# def import_graduationReq(request):
#     json_text = [{"number": "1", "content": "工程知识：能够将数学、自然科学、软件工程基础知识、软件专业知识及相关应用领域的知识用于解决复杂软件工程问题。 "},
#      {"number": "2", "content": "问题分析：能够应用数学、自然科学和软件工程科学的基本原理，识别、表达并通过文献研究分析复杂软件工程问题，以获得有效结论。 "}]
#
#     #Delete all from database before insert
#     GraduationReq.objects.all().delete()
#     for item in json_text:
#         obj = GraduationReq.objects.create(number=item["number"], content=item["content"])
#         obj.save()
#     return HttpResponse('OK')
#
# def import_graduationReqPoint(request):
#     json_text = [{"number":"1-1","GraduationReq":"1","content":"能够将数理知识、软件工程基础知识、软件专业 知识及相关领域知识用于复杂软件问题的理解和表述。"},{"number":"1-2","GraduationReq":"1","content":"能够综合相关知识，针对复杂软件问题进行建模。 "},{"number":"1-3","GraduationReq":"1","content":"能够综合相关知识，对复杂软件问题模型进行推 演和分析，从而解决复杂软件工程问题。"},{"number":"2-1","GraduationReq":"2","content":"通过运用相关科学原理，具备把整体分解为部分来认识事物的能力，也具有由部分结合形成整体来认识事物的能力，能够发现和掌握关键问题所在。"},{"number":"2-2","GraduationReq":"2","content":"针对复杂软件工程问题，能分析文献寻求解决方案并进行正确表达。"},{"number":"2-3","GraduationReq":"2","content":"对复杂软件工程问题，能够分析、比较多种解决方案，挑选出最适当的方案，做出有利于推进工作的明晰决定。"}]
#
#     # Delete all from database before insert
#     GraduationReqPoint.objects.all().delete()
#     for item in json_text:
#         graduationReq = GraduationReq.objects.get(number=item["GraduationReq"])
#         obj = GraduationReqPoint.objects.create(number=item["number"], content=item["content"],GraduationReq=graduationReq)
#         obj.save()
#
#     return HttpResponse('OK')
#
# def import_course(request):
#     json_text = [{"courseNumber":"140011","name":"微积分"},{"courseNumber":"140013","name":"线性代数"},{"courseNumber":"191101","name":"离散数学"},{"courseNumber":"140072","name":"概率论与数理统计"},{"courseNumber":"120021","name":"基础物理学"},{"courseNumber":"181101","name":"程序设计基础"},{"courseNumber":"191102","name":"数据结构"},{"courseNumber":"191104","name":"数字逻辑"},{"courseNumber":"191107 ","name":"操作系统"},{"courseNumber":"191108","name":"数据库系统"},{"courseNumber":"191109","name":"计算机网络"},{"courseNumber":"191112","name":"UML"},{"courseNumber":"191113","name":"ERP原理和SAP ERP"},{"courseNumber":"192105","name":"方向专业选修课程"},{"courseNumber":"191106","name":"软件工程"},{"courseNumber":"193107","name":"程序设计实训"},{"courseNumber":"191105","name":"计算机组成原理"},{"courseNumber":"193104","name":"软件综合实践"},{"courseNumber":"193108","name":"软件进阶实习实践"}]
#
#     # Delete all from database before insert
#     Course.objects.all().delete()
#     for item in json_text:
#         obj = Course.objects.create(courseNumber=item["courseNumber"], name=item["name"])
#         obj.save()
#     return HttpResponse('OK')
#
# def import_supportMatrix(request):
#     json_text = [{"course":"140011","point":"1-1","weight":0.3},{"course":"140013","point":"1-1","weight":0.2},{"course":"191101","point":"1-1","weight":0.2},{"course":"140072","point":"1-1","weight":0.2},{"course":"120021","point":"1-1","weight":0.1},{"course":"181101","point":"1-2","weight":0.3},{"course":"191102","point":"1-2","weight":0.3},{"course":"191104","point":"1-2","weight":0.1},{"course":"191105","point":"1-2","weight":0.1},{"course":"191107 ","point":"1-2","weight":0.2},{"course":"191108","point":"1-3","weight":0.2},{"course":"191109","point":"1-3","weight":0.2},{"course":"191112","point":"1-3","weight":0.2},{"course":"191113","point":"1-3","weight":0.2},{"course":"192105","point":"1-3","weight":0.2},{"course":"140011","point":"2-1","weight":0.15},{"course":"140013","point":"2-1","weight":0.25},{"course":"191101","point":"2-1","weight":0.25},{"course":"140072","point":"2-1","weight":0.25},{"course":"120021","point":"2-1","weight":0.1},{"course":"191102","point":"2-2","weight":0.15},{"course":"191104","point":"2-2","weight":0.1},{"course":"191109","point":"2-2","weight":0.1},{"course":"191106","point":"2-2","weight":0.15},{"course":"191108","point":"2-2","weight":0.1},{"course":"193107","point":"2-2","weight":0.15},{"course":"192105","point":"2-2","weight":0.25},{"course":"191105","point":"2-3","weight":0.1},{"course":"191107 ","point":"2-3","weight":0.2},{"course":"191113","point":"2-3","weight":0.1},{"course":"193104","point":"2-3","weight":0.3},{"course":"193108","point":"2-3","weight":0.3}]
#
#     # Delete all from database before insert
#     SupportMatrix.objects.all().delete()
#     for item in json_text:
#         course = Course.objects.get(courseNumber=item["course"])
#         point = GraduationReqPoint.objects.get(number=item["point"])
#
#         obj = SupportMatrix.objects.create(course=course, point=point,weight=item["weight"])
#         obj.save()
#     return HttpResponse('OK')


def import_data(request):
    return render(request,'majorPerson/import_supportMatrix.html')

def import_interface(request):
    info = json.loads(request.POST['info'])
    req = info["req"]
    point = info["point"]
    course = info["course"]
    point_course_matrix = info["point_course_matrix"]

    # Delete all from database before insert
    GraduationReq.objects.all().delete()
    for item in req:
        obj = GraduationReq.objects.create(number=item["number"], content=item["content"])
        obj.save()

    # Delete all from database before insert
    GraduationReqPoint.objects.all().delete()
    for item in point:
        graduationReq = GraduationReq.objects.get(number=item["GraduationReq"])
        obj = GraduationReqPoint.objects.create(number=item["number"], content=item["content"],GraduationReq=graduationReq)
        obj.save()

    # Delete all from database before insert
    Course.objects.all().delete()
    for item in course:
        obj = Course.objects.create(courseNumber=item["courseNumber"], name=item["name"])
        obj.save()

    # Delete all from database before insert
    SupportMatrix.objects.all().delete()
    for item in point_course_matrix:
        course = Course.objects.get(courseNumber=item["course"])
        point = GraduationReqPoint.objects.get(number=item["point"])

        obj = SupportMatrix.objects.create(course=course, point=point,weight=item["weight"])
        obj.save()
    return render(request,'majorPerson/import_supportMatrix.html')

def get_matrix(request):
    graduationReq_point_number = request.POST['point']
    #Return
    #courseNumber/courseName/weight
    result = SupportMatrix.objects.filter(point__number=graduationReq_point_number)
    data = []
    for item in result:
        courseNumber = item.course.courseNumber
        courseName = item.course.name
        weight = item.weight
        temp = {
            "courseNumber":courseNumber,
            "courseName":courseName,
            "weight":weight
        }
        data.append(temp)
    data = json.dumps(data, ensure_ascii=False)
    return HttpResponse(data)
