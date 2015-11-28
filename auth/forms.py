from django import forms

class LogInForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=256)
    password = forms.CharField(label="Password", max_length=256, widget=forms.PasswordInput())

