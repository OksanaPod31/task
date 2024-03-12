from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Task, Entry
from .forms import TaskForm, EntryForm
# Create your views here.


def index(request):
    """Домашняя страница приложения Task"""
    return render(request, 'tasks/index.html')


@login_required
def tasks(request):
    """Выводит список тем."""
    tasks = Task.objects.filter(owner=request.user).order_by('task_name')
    context = {'tasks': tasks}
    return render(request, 'tasks/tasks.html', context)


@login_required
def task(request, task_id):
    """Выводит одну задачу и все ее записи."""
    task = Task.objects.get(id=task_id)
    # Проверка того, что тема принадлежит текущему пользователю.
    if task.owner != request.user:
        raise Http404
    entries = task.entry_set.order_by('start_time')
    context = {'task': task, 'entries': entries}
    return render(request, 'tasks/task.html', context)


@login_required
def new_task(request):
    """Определяет новую задачу."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = TaskForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('tasks:tasks')
    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'tasks/new_task.html', context)


@login_required
def new_entry(request, task_id):
    """Добавляет новую запись по конкретной задаче."""
    task = Task.objects.get(id=task_id)
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = EntryForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.task = task
            new_entry.save()
            return redirect('tasks:task', task_id=task_id)
    # Вывести пустую или недействительную форму.
    context = {'task': task, 'form': form}
    return render(request, 'tasks/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """Редактирует существующую запись."""
    entry = Entry.objects.get(id=entry_id)
    task = entry.task
    if task.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Исходный запрос; форма заполняется данными текущей записи.
        form = EntryForm(instance=entry)
    else:
        # Отправка данных POST; обработать данные.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task', task_id=task.id)
    context = {'entry': entry, 'task': task, 'form': form}
    return render(request, 'tasks/edit_entry.html', context)
