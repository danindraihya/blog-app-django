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
        read_only_fields = [
            'slug',
            'author'
        ]

    def validate_title(self, value):
        qs = Posts.objects.filter(title__iexact=value)
        if self.instance:
            qs = qs.exclude(pk=self.instance)
        if qs.exists():
            raise serializers.ValidationError("The title must be unique")
        return value
