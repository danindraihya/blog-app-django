from django.contrib import admin
from django.urls import path, include
from .views import (
    HomeView
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('post/', include(('post.urls', 'post'), namespace='post')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    path('api/post/', include(('post.api.urls', 'post/api'), namespace='api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)