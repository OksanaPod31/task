from django import forms
from .models import Task, Entry


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['task_name']
        labels = {'task_name': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['start_time', 'end_time', 'completed', 'priority']
        labels = {'start_time': 'Start Time', 'end_time': 'End_Time',
                  'completed': 'Completed', 'priority': 'Priority'}
        widgets = {'start_time': forms.DateInput(
            attrs={'type': 'date'}), 'end_time': forms.DateInput(attrs={'type': 'date'})}
