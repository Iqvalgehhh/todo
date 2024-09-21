#a4
from django.shortcuts import render
#a12
from todo.models import Task

#a3
def home(request):
    #a11
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    #a13
    context = {
        'tasks' : tasks, 
    }
    return render(request, 'home.html', context)