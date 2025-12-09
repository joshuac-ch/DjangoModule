from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import Task,Usuarios

# Create your views here.

def About(request):
    nombre="ninodev"
    return render(request,'index.html',{'name':nombre})

def Contact(request,us):
    return HttpResponse(f"Contactat {us}")

def Tareas(request,id):
    #task=get_object_or_404(Task,id=id)
    task2=Task.objects.get(id=id)
    return render(request,'task.html',{"task":task2})

def FecthUser(request):
    user=Usuarios.objects.all()
    return render(request,'Users.html',{"user":user})