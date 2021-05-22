from django import forms
from django.forms import ModelForm
from .models import Task, User

class SignUp(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    re_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class SignIn(forms.Form):
    # username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=50, widget=forms.PasswordInput)
    # re_password = forms.CharField(max_length=50, widget=forms.PasswordInput)

class Task_form(forms.Form):
    task = forms.CharField(max_length=80,widget = forms.TextInput(attrs={'placeholder':"Enter Your Task","class":"task_input"}))

    # class Meta:
    #     model = Task
    #     fields = '__all__'