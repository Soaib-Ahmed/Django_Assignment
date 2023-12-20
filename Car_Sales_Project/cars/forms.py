from django import forms
from .models import Car,CarComment

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = CarComment
        fields = ['name', 'body']
