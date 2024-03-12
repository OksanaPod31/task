"""Определяет схемы URL для learning_logs."""

from django.urls import path
from . import views

app_name = 'tasks'
urlpatterns = [
    # Домашняя страница
    path('', views.index, name='index'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/', views.task, name='task'),
    path('new_task/', views.new_task, name='new_task'),
    path('new_entry/<int:task_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
