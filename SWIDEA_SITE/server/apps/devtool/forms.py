from django import forms
from .models import Devtool



class DevtoolForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = '__all__'
        labels = {
            'dev_name': '이름',
            'dev_type': '종류',
            'dev_content': '개발툴 설명'
        }