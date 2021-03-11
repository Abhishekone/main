from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def the(request):
    return render(request,'app2/the.html')
