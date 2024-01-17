from django.db import models
from apps.devtool.models import Devtool 

class Post(models.Model) : 
    title = models.CharField('아이디어명', max_length=24)
    content = models.CharField('아이디어 설명', max_length=1000)
    interest = models.IntegerField('아이디어 관심도', default=0)
    
    #개발 툴 
    devtool = models.ForeignKey(Devtool, on_delete=models.SET_NULL, null=True, verbose_name='예상 개발툴')

    #수정전 코드 : devtool = models.ForeignKey(Devtool, on_delete=models.CASCADE, verbose_name='예상 개발툴')
    # user = models.ForeignKey(LocalUser, on_delete=models.CASCADE, verbose_name='작성자')
    #local_users의 models.py애 LocalUser와 연결

    #찜하기

    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    
    #아이디어 관심도 + 4 -
    
    #이미지
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    
    def __str__(self):
        return f'[아이디어] {self.title}'
