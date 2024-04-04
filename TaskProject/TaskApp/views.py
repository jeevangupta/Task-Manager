from django.shortcuts import redirect, render
from .models import Tasks
from django.contrib import messages
# Create your views here.

def my_task(request):
    
    all_tasks = Tasks.objects.all().order_by("title")

    data = {"all_tasks":all_tasks}
    #messages.success(request, 'Test')
    return render(request, "./task_app/my_task.html", data)


def create_task(request):
    if request.method == 'POST':
        task_title = request.POST.get("taskTitle",None)
        task_description = request.POST.get("taskDescription",None)
        task_status = request.POST.get("taskStatus",None)

        task = Tasks(title= task_title, description = task_description, status = task_status)

        try:
            task.save()
            messages.success(request, 'Task created successfully!')
        except Exception as e:
            messages.success(request, f'Failed to create Task! {str(e)}')
    else:
        messages.error(request, f"Invalid method")

    data = {"message":"Test"}

    return redirect('my-task')


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


