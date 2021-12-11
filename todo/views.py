from django.shortcuts import render
from django.views.decorators.http import require_POST

from .forms import TaskForm
from .models import Task


def home(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            tasks = Task.objects.filter(user=request.user)
        else:
            tasks = None
        form = TaskForm()
        context = {
            "tasks": tasks,
            "form": form,
            "error": None,
        }
        return render(request, "home.html", context)
    else:
        form = TaskForm(request.POST)
        tasks = Task.objects.filter(user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            context = {
                "tasks": tasks,
                "form": TaskForm(),
                "error": None,
            }
            return render(request, "components/tasks.html", context)
        else:
            errors = form.errors
            context = {
                "tasks": tasks,
                "error": errors,
            }

            return render(request, "components/task_list.html", context)


@require_POST
def complete(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.done == True:
        task.done = False
    else:
        task.done = True
    task.save()
    tasks = Task.objects.filter(user=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "components/task_list.html", context)


@require_POST
def delete(request, task_id):
    Task.objects.filter(id=task_id).delete()
    tasks = Task.objects.filter(user=request.user)
    context = {
        "tasks": tasks,
    }
    return render(request, "components/task_list.html", context)


def auth(request):
    return render(request, "components/auth.html")
