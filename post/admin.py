from django.contrib import admin
from .models import Posts

class AdminPost(admin.ModelAdmin):
    readonly_fields = [
        'slug'
    ]

admin.site.register(Posts, AdminPost)