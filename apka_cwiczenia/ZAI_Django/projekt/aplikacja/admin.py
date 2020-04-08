from django.contrib import admin
from . import models
from .models import Questions,Choice
# Register your models here.
admin.site.register(models.Questions)
admin.site.register(models.Choice)