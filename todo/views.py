#a21
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


#a20
def addTask(request):
    #a25
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')