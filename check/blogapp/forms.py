from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pagedown.widgets import *


class BlogForm(forms.ModelForm):
    content = forms.CharField(widget = PagedownWidget)
    
    class Meta:
        model = Blog
        fields=('title','content','image',)


    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs={'class':'form-control','placeholder':'Title'}
        self.fields['content'].widget.attrs={'class':'form-control','placeholder':'Content'}

class DetailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password',)


class ProfileForm(forms.ModelForm):

    class Meta:
        model=Profile
        exclude=['user']
