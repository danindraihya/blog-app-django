from django.urls import path
from .views import (
    ListPostsView
)

urlpatterns = [
    path('', ListPostsView.as_view(), name='list'),
]
