from django.shortcuts import render
from todo.models import Task

def tasks(request):
    tasks= Task.objects.filter(is_completed=False).order_by('-updated_at')

    completed_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')

    incomplete_tasks = Task.objects.filter(incomplete=True).order_by('-updated_at')
    
    context = {
    'tasks': tasks,
    'completed_tasks': completed_tasks,
    'incomplete_tasks': incomplete_tasks,
    }
    return render(request, 'home.html', context)