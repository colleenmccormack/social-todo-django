from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(label='task name', max_length=5000)
    task_description = forms.CharField(label='task description', max_length=5000)
    collaborator = forms.CharField(label='collaborator', max_length=5000)