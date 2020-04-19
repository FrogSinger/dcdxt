from django.shortcuts import render

# Create your views here.
# /coursePerson/index
def index(request):
    return render(request,'coursePerson/index.html')

def get_examine(request):
    return render(request, 'coursePerson/course_value.html')