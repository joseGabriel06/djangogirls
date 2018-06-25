from django.urls import path
from .views import PostListView, PostCreateView,PostDeleteView


urlpatterns = [
    path('', PostListView.as_view(), name='index' ),
    path('create_post/', PostCreateView.as_view(
         template_name='includes/edit.html'
        ),name='create_post'),
    path('post_edit/<int:pk>/', PostDeleteView.as_view(),name='detail')
]
