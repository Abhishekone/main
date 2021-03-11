from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def zero(request):
    return render(request,'app/bye.html')

#def two(request):
    return render(request,'app/mas.html')


