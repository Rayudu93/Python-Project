from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')  # 👈 user-specific
    return render(request, 'home.html', {'tasks': tasks})
@login_required
def add_task(request):
    if request.method == 'POST':
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text, user=request.user)  # 👈 set user here
    return redirect('/')


def delete_task(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')
