from django.db import models
from api.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title