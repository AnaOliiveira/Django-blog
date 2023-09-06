from django.urls import path
from blog.views import (index, ola, get_all_posts, get_post, PostDetailView)


urlpatterns = [
    path('', index, name= "home"),
    path('index/', index, name= "index"),
    path('ola/', ola, name= "ola"),
    path('posts/all', ola, name="posts_list"),
    path('posts/all', ola, name="posts_list"),
    path('post/<int:post_id>', post_show, name="exibe_post"),
    path('post/<int:pk>/show', PostDetailView.as_view(), name="post_detail"),
    path('api/posts', get_all_posts, name="posts_data"),
    path('api/posts/<int:post_id>', get_post, name="post_data"),
]
