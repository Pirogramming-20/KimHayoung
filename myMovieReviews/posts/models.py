from django.db import models

#리뷰 리스트 페이지에 개요 : 각 영화 제목, 개봉연도, 장르, 별점, 리뷰내용
class Post(models.Model) :
    movie_title = models.CharField(max_length=32)
    created_year = models.TextField()
    genre = models.CharField(max_length=32)
    score = models.CharField(max_length=32)
    #charfield말고 더 적절한거 있으려나? max_length도 애매하네.
    review_content = models.TextField()

    #새로 추가해본 내용
    director = models.CharField(max_length=32)
    actor = models.CharField(max_length=32)
    running_time = models.TextField()


#코멘트를 만들어보자. ! 사이트 ctrl c 한다음, migrations도 까먹지 말고 해주기. 
class Comment(models.Model) : 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    
