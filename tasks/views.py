from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Tag

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
