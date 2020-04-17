from django.shortcuts import render

# /student/index
def index(request):
    return render(request,'student/index.html')