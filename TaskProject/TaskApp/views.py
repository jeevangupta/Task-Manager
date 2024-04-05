from django.shortcuts import redirect, render, HttpResponse
from .models import Tasks
from django.contrib import messages
from django.urls import reverse
from UserApp.auth_decorator import login_required

def home(request):
    data = {}
    return render(request, './task_app/home.html', data)

@login_required
def my_task(request):
    data = {}
    if request.method == 'GET':
        all_tasks = Tasks.objects.all().order_by("title")

        data = {"all_tasks":all_tasks}
    else:
        messages.error(request, f"Invalid method")

    return render(request, "./task_app/my_task.html", data)


@login_required
def create_task(request):
    if request.method == 'POST':
        task_title = request.POST.get("taskTitle",None)
        task_description = request.POST.get("taskDescription",None)
        task_status = request.POST.get("taskStatus",None)

        if task_title:
            if task_status in ["To Do","In Progress", "Done"]:
                task = Tasks(title= task_title, description = task_description, status = task_status)

                try:
                    task.save()
                    messages.success(request, 'Task created successfully!')
                except Exception as e:
                    messages.success(request, f'Failed to create Task! {str(e)}')
            else:
                messages.success(request, 'Failed to create Task! Invalid task status')
        else:
            messages.success(request, 'Failed to create Task! Title cannot be empty')
    else:
        messages.error(request, "Invalid method")

    #data = {"message":"Test"}

    return redirect('my-task')


@login_required
def delete_task(request):
    if request.method == 'POST':
        task_id = request.POST.get("task-id",None)

        task = Tasks.objects.filter(id=task_id).first()
        
        if task:
            try:
                task.delete()
                messages.success(request, 'Task deleted successfully!')
            except Exception as e:
                messages.success(request, f'Failed to delete Task! {str(e)}')
        else:
            messages.error(request, f"No task found to delete!")
    else:
        messages.error(request, f"Invalid method")

    return redirect('my-task')


@login_required
def update_task(request):
    if request.method == 'POST':
        task_id = request.POST.get("task-id",None)
        new_status = request.POST.get("newStatus",None)

        task = Tasks.objects.filter(id=task_id).first()
        if task:
            try:
                task.status = new_status
                task.save()
                messages.success(request, 'Task status updated successfully!')
            except Exception as e:
                messages.success(request, f'Failed to update task! {str(e)}')
        else:
            messages.error(request, f"Task not found")
    else:
        messages.error(request, f"Invalid method")

    return redirect('my-task')


