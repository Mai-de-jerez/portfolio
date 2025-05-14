from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget
from django.core.validators import MinValueValidator


class PostForm(forms.ModelForm):
    order = forms.IntegerField(
    validators=[MinValueValidator(0)],
    widget=forms.NumberInput(attrs={'min': '0',
                'class': 'form-control'})),
    content = forms.CharField(
        label='Contenido',
        widget=CKEditor5Widget(config_name='default', attrs={'style': 'color:black'}))
    

    class Meta: 
        model = Post
        fields = ['title', 'content', 'image', 'categories', 'order']
        widgets = {
        'order': forms.NumberInput(attrs={
            'min': '0', 
            'style': 'background-color: white; color: black; width: 50px; border: 1px solid #ccc;',
            'class': 'form-control'}),
        }
        
        

    
    
        

      

 

    