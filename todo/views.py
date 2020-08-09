from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'tasks': tasks, 'form': form}
    return render(request, 'todo/index.html', context)

def completed(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('/')

def deleteAllCompleted(request):
    tasks = Task.objects.filter(complete=True)
    for task in tasks:
        task.delete()
    return redirect('/')
