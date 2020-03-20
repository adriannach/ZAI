from datetime import datetime
from django.conf import settings
from django.db import models
from ckeditor.fields import RichTextField

def upload_loc(instance, filename):
    filename = datetime.now()
    return "%s/%s" %(instance.id, filename)

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    image = models.ImageField(upload_to=upload_loc, null=True, blank=True)
    body = RichTextField(blank=True, null=True)
    mini_body = models.TextField(max_length=500, blank=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)