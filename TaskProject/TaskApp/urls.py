from django.urls import path
from .views import (my_task, create_task, delete_task, update_task)

urlpatterns = [
    path(r"my-task", my_task, name="my-task"),

    path(r"create-task", create_task, name="create-task"),

    path(r"delete-task", delete_task, name="delete-task"),

    path(r"update-task", update_task, name="update-task"),

]