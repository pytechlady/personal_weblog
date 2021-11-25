from django import forms
from .models import Blogs


class Createform(forms.ModelForm):    

    class Meta:
        model= Blogs
        fields= ['blog_title',
                 'description', 'author', 'blog_tag']