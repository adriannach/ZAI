from rest_framework.serializers import ModelSerializer

from recipes.models import Recipe

class RecipeIndexSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'user', 'title', 'body', 'mini_body', 'created_at', 'updated_at']

class RecipeShowSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'body', 'mini_body', 'created_at', 'updated_at']

class RecipeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'body', 'mini_body', 'created_at', 'updated_at']
