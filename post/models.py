from django.db import models

class Posts(models.Model):
    title       = models.CharField(max_length=255)
    content     = models.TextField(max_length=255)
    created_at  = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
