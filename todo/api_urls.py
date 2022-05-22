from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("tasks/", views.tasks, name="tasks-api"),
    path("tasks/<int:task_id>/", views.task, name="task-api"),
]
