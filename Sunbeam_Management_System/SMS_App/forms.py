from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import admin


class admin_signup(UserCreationForm):
    class Meta:
        model = admin
        fields = ['first_name', 'last_name',
                  'email', 'employee_num', 'username', 'password1', 'password2']
