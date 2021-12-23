from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Photo



class CustomUserCreationForm(UserCreationForm):
    class Meta():
        model = User
        fields = ['username','password1','password2']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control','placeholder':'Enter username..'})
        self.fields['password1'].widget.attrs.update({'class':'form-control'})
        self.fields['password2'].widget.attrs.update({'class':'form-control'})

class CustomPhoto(forms.ModelForm):
    class Meta():
        model = Photo
        fields = ['description','image']

    def __init__(self, *args, **kwargs):
        super(CustomPhoto,self).__init__(*args,**kwargs)
        self.fields['description'].widget.attrs.update({'class':'my-col-7'})
        self.fields['image'].widget.attrs.update({'class':'my-image'})
