from django import forms
from .models import Profile,Art,Comments
from django.forms import ModelForm,Textarea,IntegerField

class NewArtForm(forms.ModelForm):
    class Meta:
        model = Art
        exclude = ['user','arts']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','arts']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['posted_by', 'commented_art','user']
        
