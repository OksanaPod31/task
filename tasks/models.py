from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Task(models.Model):
    """Задача пользователя"""
    task_name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.task_name


class Entry(models.Model):
    """Описание задачи"""
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    start_time = models.DateField(auto_now_add=False)
    end_time = models.DateField(auto_now_add=False)
    completed = models.BooleanField(default=False)
    priority = models.CharField(max_length=10, choices=(
        ("high", "High"), ("medium", "Medium"), ("low", "Low")))

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возвращает строковое представление модели."""
        return f"{self.task}"
