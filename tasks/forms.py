from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(label='task name', max_length=5000)
    task_description = forms.CharField(label='task description', max_length=5000)
    collaborator = forms.CharField(label='collaborator', max_length=5000)

class NameForm(forms.Form):
    your_name = forms.CharField(label='Name:', max_length=100)
    your_email = forms.CharField(label='Email:', max_length=100)
    your_password = forms.CharField(label='Password:', max_length=100)