from django.urls import path
from .views import PostListView, PostCreateView,PostDetailView


urlpatterns = [
    path('', PostListView.as_view(), name='index' ),
    path('create_post/', PostCreateView.as_view( template_name='blog/post_edit.html'),name='create_post'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='detail')
]
