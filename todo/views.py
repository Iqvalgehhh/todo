#a21
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task


#a20
def addTask(request):
    #a25
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

#a29
def mark_as_done(request, pk):
    #a31
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


#a32
def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

#a34
def edit_task(request, pk):
    #a36
    get_task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        #a39
        new_task = request.POST['task']
        get_task.task = new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

