from rest_framework import generics
from post.models import Posts
from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'pk'
    # queryset            = 
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return Posts.objects.all()

