from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
# Create your models here.
from recipes.models import Recipe


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
    recipe = models.ForeignKey(Recipe, default=1, on_delete=models.CASCADE)
    body = models.CharField(max_length=500)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
