from django.contrib import admin

# Register your models here.

from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at','updated_at']
    list_display_links = ['updated_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'body']
    class Meta:
        model = Recipe


admin.site.register(Recipe, RecipeAdmin)  # dodanie przepisów do admina
