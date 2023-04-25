from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Fish

# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj1 = Fish.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj1})
#
# def operations(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     Ares = x + y
#     Sres = x - y
#     Mres = x * y
#     Dres = x / y
#     return render(request,'result.html',{'add':Ares,'sub':Sres,'mul':Mres,'div':Dres})
