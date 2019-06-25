from django import forms
from .models import Task, Cheklist
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content', 'stasus_in_percents', 'deadline')

class CheklistForm(forms.ModelForm):
    class Meta:
        model = Cheklist
        fields = ('body','id')

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError("This email already used")
        return data