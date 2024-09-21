#a4
from django.shortcuts import render
#a12
from todo.models import Task

#a3
def home(request):
    #a11
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')

    #a26
    completed_tasks = Task.objects.filter(is_completed=True)

    #a13
    context = {
        #yg pertama bikinan sendiri, yg kedua dari atas (variabel)
        'tasks' : tasks, 
        'completed_tasks' : completed_tasks
    }
    return render(request, 'home.html', context)