# home/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    # Map the form field names to the HTML input names
    login_email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'login_email', 'placeholder': 'name@example.com'})
    )
    login_password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'login_password', 'placeholder': 'Enter your password'})
    )
    remember = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'id': 'remember'})
    )

    # Rename the fields for internal use
    def clean(self):
        cleaned_data = super().clean()
        # Map login_email to email for use in the view
        cleaned_data['email'] = cleaned_data.get('login_email')
        cleaned_data['password'] = cleaned_data.get('login_password')
        return cleaned_data