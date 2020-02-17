from django.shortcuts import render
from django.views.generic import ListView
from .models import Posts

class ListPostsView(ListView):
    model         = Posts
    template_name = 'post/list.html'
    context_object_name = 'list_post'
