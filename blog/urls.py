from django.urls import path
from .views import PostListView, PostDetailView, PostUpdate, PostCreate, PostsByCategoryView, PostDelete


post_patterns = ([
    path("", PostListView.as_view(), name="post_list"), 
    path("create/", PostCreate.as_view(), name="create"),
    path('category/<int:category_id>/', PostsByCategoryView.as_view(), name='posts_by_category'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='post_delete'),

], "blog")


