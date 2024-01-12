from django.urls import path, include
from .views import *

urlpatterns = [
    path('', post_list),
    path('<int:pk>', posts_detail),
    path('create', posts_create),
    path('<int:pk>/update', posts_update),
    path('<int:pk>/delete', posts_delete),
    # path('<int:post_id>/comments/create', comments_create),

]