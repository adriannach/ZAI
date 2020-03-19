from django.db import models


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    body = models.TextField(max_length=1000)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)