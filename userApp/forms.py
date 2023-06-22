from django import forms
from .models import Posts

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('caption', 'image')
        widgets = {
            'caption': forms.Textarea(attrs={'class': 'custom-input', 'placeholder': 'Enter your caption'}),
        }
