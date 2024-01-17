from django import forms
from .models import Post 

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('__all__')
        labels = {
            'content': '아이디어 설명',
            'interest': '아이디어 관심도'
        }
           
        