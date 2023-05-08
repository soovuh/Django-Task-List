from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Task
from .forms import NewTaskForm, EditTaskForm


@login_required
def list(request):
    user_tasks = Task.objects.filter(created_by=request.user).order_by('-created_at')
    

    return render(request, 'tasks/list.html', {
        'tasks' : user_tasks,
    })


@login_required
def new_task(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('tasks:list')
    else:
        form = NewTaskForm()
    return render(request, 'tasks/new.html', {
        'form': form
    })


@login_required
def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)

    task.is_complete = True
    task.save()

    return redirect('tasks:list')


@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)

    if request.method =='POST':
        form = EditTaskForm(request.POST, request.FILES, instance=task)

        if form.is_valid():
            form.save()
            return redirect('tasks:list')
    else:
        form = EditTaskForm(instance=task)

    return render(request, 'tasks/new.html', {
        'form': form
    })


@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, created_by=request.user)
    task.delete()

    return redirect('tasks:list')
