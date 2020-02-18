from django.shortcuts import render
from django.views.generic import (
    ListView,
    DeleteView,
    UpdateView,
    CreateView,
    UpdateView,
    DetailView
    )
from .models import Posts
from django.urls import reverse_lazy
from .forms import PostForm

class ListPostsView(ListView):
    model         = Posts
    template_name = 'post/list.html'
    context_object_name = 'list_post'

class DeletePostsView(DeleteView):
    model           = Posts
    template_name   = 'post/delete_confirmation.html'
    success_url     = reverse_lazy('post:list')

class CreatePostsView(CreateView):
    form_class      = PostForm
    template_name   = 'post/create.html'

class UpdatePostsView(UpdateView):
    form_class      = PostForm
    model           = Posts
    template_name   = 'post/update.html'

class DetailPostsView(DetailView):
    model           = Posts
    template_name   = 'post/detail.html'