from django.shortcuts import render

# Create your views here.
#/instructor/index
def index(request):
    return render(request,'instructor/index.html')