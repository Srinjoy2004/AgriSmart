from django import forms
from .models import User

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'name@example.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Enter your password'}))
    remember = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'remember'}))

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'password', 'placeholder': 'Enter your password'}))
    class Meta:
        model = User
        fields = ['user_name', 'user_phone', 'user_email', 'user_password']
        widgets = {
            'user_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter your name'}),
            'user_phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'phone', 'placeholder': 'Enter your phone number'}),
            'user_email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'name@example.com'}),
        }