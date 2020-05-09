from django.forms import ModelForm
from django import forms
from .models import choices

class movie_choices_form(ModelForm):
    movie_1 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    movie_2 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    movie_3 = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
        }
    ))
    
    class Meta:
        model = choices
        fields = ['movie_1','movie_2','movie_3']
    
    # widgets = {
    #     'movie_1': forms.TextInput(attrs={'class':'form-control'}),
    #     'movie_2': forms.TextInput(attrs={'class':'form-control'}),
    #     'movie_3': forms.TextInput(attrs={'class':'form-control'}),
    # }