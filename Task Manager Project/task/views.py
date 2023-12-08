from django.shortcuts import render,get_object_or_404,redirect
from . import forms
from .models import Task
from category.models import TaskCategory

def show_tasks(request):
    tasks = Task.objects.all()
    categories = TaskCategory.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks, 'categories': categories})

def add_task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm()
    
    return render(request, 'add_task.html', {'form': task_form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('show_tasks')
    else:
        task_form = forms.TaskForm(instance=task)

    return render(request, 'edit_task.html', {'form': task_form, 'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('show_tasks')
