from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput(), min_length=8)