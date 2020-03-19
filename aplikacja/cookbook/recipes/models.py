from datetime import datetime

from django.db import models

def upload_loc(instance, filename):
    filename = datetime.now()
    return "%s/%s" %(instance.id, filename)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return self.title
    image = models.ImageField(upload_to=upload_loc, null=True, blank=True)
    body = models.TextField(max_length=10000)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)