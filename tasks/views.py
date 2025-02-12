   # tasks/views.py
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    """View to display the list of tasks."""
    tasks = Task.objects.all()  # Fetch all tasks from the database
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/edit_task.html', {'form': form})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

class TaskViewSet(viewsets.ModelViewSet):
    """API View to handle CRUD operations for Task model."""
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
'''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Tag

#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth import login

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    if request.method == 'POST':
        # Get the task and the new status from the form
        task_id = request.POST.get('task_id')
        status = request.POST.get('status')  # New status

        # To Get the task object
        task = get_object_or_404(Task, id=task_id, user=request.user)

        # To Update the status of the task
        task.status = status
        task.save()

        return redirect('task_list')  # Redirect to refresh the task list view

    return render(request, 'tasks/task_list.html', {'tasks': tasks})  # Pass tasks to the template


@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status', 'pending')  # Get status from form
        tags = request.POST.getlist('tags')  # Get multiple selected tags

        # Create the task with the provided information
        task = Task.objects.create(
            title=title,
            description=description,
            category=category,
            due_date=due_date,
            status=status,  
            user=request.user
        )

        # Add tags to the created task
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            task.tags.add(tag)

        return redirect('task_list')  # Redirect to task list view after adding the task

    tags = Tag.objects.all()  # Retrieve all available tags for the form
    return render(request, 'tasks/add_task.html', {'tags': tags})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()  # Delete the task
    return redirect('task_list')

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        # Get updated task details from the form
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.category = request.POST.get('category')
        task.due_date = request.POST.get('due_date')
        task.status = request.POST.get('status')

        # Update task tags
        tags = request.POST.getlist('tags')
        task.tags.clear()  # Clear existing tags
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            task.tags.add(tag)

        # Save updated task
        task.save()
        return redirect('task_list')  # Redirect back to the task list

    tags = Tag.objects.all()  # Retrieve all available tags for the form
    return render(request, 'tasks/edit_task.html', {'task': task, 'tags': tags})

#def register(request):
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #   if form.is_valid():
    #       user = form.save()
    #       login(request, user)
    #       return redirect('task_list')  # Redirect to task list after registration
    #else:
    #   form = UserCreationForm()
    #return render(request, 'register.html', {'form': form})'''

 



