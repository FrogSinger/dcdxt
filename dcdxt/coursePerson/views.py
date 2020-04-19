from django.shortcuts import render

# Create your views here.
# /coursePerson/index
def index(request):
    return render(request,'coursePerson/index.html')