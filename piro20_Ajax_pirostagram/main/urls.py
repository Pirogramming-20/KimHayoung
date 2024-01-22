from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post_new/', views.post_new, name='post_new'),
    path('like_ajax/', views.like_ajax, name='like_ajax'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
]
#/post_new