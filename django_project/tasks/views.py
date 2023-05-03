from django.shortcuts import render, get_list_or_404
from django.contrib.auth.decorators import login_required

from .models import Task


@login_required
def list(request):
    user_tasks = Task.objects.filter(created_by=request.user)

    return render(request, 'tasks/list.html', {
        'tasks' : user_tasks,
    })
