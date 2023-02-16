from pickle import GET
from .models import Place, Meetteam
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    obj = Place.objects.all()
    team = Meetteam.objects.all()
    return render(request, 'index.html', {'result': obj,'result1': team})


#def answer(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
  #  res1=x+y
   # res2=x-y
    #res3=x*y
    #res4=x/y
    #return render(request,'result.html',{'answer1':res1,'answer2':res2,'answer3':res3,'answer4':res4,})

