from rest_framework import serializers
from post.models import Posts

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Posts
        fields  = [
            'pk',
            'title',
            'content',
            'slug',
            'author',
            'created_at'
        ]
