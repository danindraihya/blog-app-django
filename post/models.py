from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class Posts(models.Model):
    title       = models.CharField(max_length=255)
    content     = models.TextField(max_length=255)
    slug        = models.SlugField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Posts, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post:list')