from django import forms
from TaskTamer import models
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm

from django.utils import timezone


class TasksForm(forms.ModelForm):
    class Meta:
        model = models.Tasks
        fields = '__all__'

class User_TasksForm(forms.ModelForm):
    class Meta:
        model = models.User_Tasks
        fields = '__all__'

class UserForm(UserCreationForm):
    email = forms.EmailField(max_length=150)


# ctrl +shift + F



class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profil
        fields = ['avatar']

