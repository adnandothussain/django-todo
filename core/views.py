import uuid
from django.shortcuts import redirect, render
from .models import Task
# Create your views here.


def todos(request):
    if request.method == 'GET':
        todos = Task.objects.all().values()
        return render(request, 'index.html', {'todos': todos})
    if request.method == 'POST':
        todo = request.POST["todo"]
        task = Task.objects.create(
            user=request.user, title=todo, desciption='')
        task.save()
        return redirect('/')


def update_todo(request, id):
    # if request.method != 'PUT':
    #     return redirect('/')
    todo = Task.objects.get(id=uuid.UUID(id))
    todo.complete = not todo.complete
    todo.save()
    return redirect('/')


def delete_todo(request, id):
    if request.method != 'DELETE':
        return redirect('/')
    todo = Task.objects.get(id=id)
    todo.delete()
    return redirect('/')
