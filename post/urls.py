from django.urls import path
from .views import (
    ListPostsView,
    DeletePostsView,
    CreatePostsView,
    DetailPostsView,
    UpdatePostsView
)

urlpatterns = [
    path('', ListPostsView.as_view(), name='list'),
    path('delete/<int:pk>', DeletePostsView.as_view(), name='delete'),
    path('create/', CreatePostsView.as_view(), name='create'),
    path('detail/<str:slug>', DetailPostsView.as_view(), name='detail'),
    path('update/<int:pk>', UpdatePostsView.as_view(), name='update'),
]
