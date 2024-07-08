from django import forms
from .models import PostDoodle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostDoodleForm(forms.ModelForm):
    class Meta:
        model = PostDoodle
        fields = ['photo', 'text']

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')