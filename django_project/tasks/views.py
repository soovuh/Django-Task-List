from django.shortcuts import render, redirect, get_list_or_404
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
def update_task(request):
    if request.method == 'POST' and request.is_ajax():
        task_id = request.POST.get('task_id')
        is_complete = request.POST.get('is_complete')
        task = Task.objects.get(id=task_id)
        task.is_complete = (is_complete == 'true')
        task.save()
        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

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


