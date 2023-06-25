from django import forms
from .models import Posts
from login_register.models import Users

class PostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('caption', 'image')
        widgets = {
            'caption': forms.Textarea(attrs={'class': 'custom-input', 'placeholder': 'Enter your caption'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('profile_image', 'bio')
        widgets = {
           'bio': forms.Textarea(attrs={'class': 'custom-input', 'placeholder': 'Enter your bio'}),
       }
        
    def __init__(self, *args, **kwargs):
        super(EditForm, self).__init__(*args, **kwargs)
        self.fields['profile_image'].required =False
        self.fields['bio'].required = False
            
        