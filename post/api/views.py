from rest_framework import generics, mixins
from post.models import Posts
from .serializers import BlogPostSerializer

class BlogPostAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field        = 'pk'
    # queryset            = 
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return Posts.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field        = 'pk'
    # queryset            = 
    serializer_class    = BlogPostSerializer

    def get_queryset(self):
        return Posts.objects.all()


