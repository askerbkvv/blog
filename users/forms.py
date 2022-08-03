from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    phone_number = forms.CharField(max_length=24)
    lessons = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'lessons', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    phone_number = forms.CharField(max_length=24)
    lessons = forms.CharField(max_length=25)

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'lessons']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']