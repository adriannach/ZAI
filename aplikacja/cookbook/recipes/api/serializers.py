from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField,
    SerializerMethodField
    )

from recipes.models import Recipe

class RecipeIndexSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(
        view_name='show_api',
        lookup_field='pk'
    )
    user = SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ['url', 'id', 'user', 'title', 'body', 'mini_body', 'created_at', 'updated_at']

    def get_user(self, obj):
        return str(obj.user.username)

class RecipeShowSerializer(ModelSerializer):
    delete_url = HyperlinkedIdentityField(
        view_name='delete_api',
        lookup_field='pk',
    )
    user = SerializerMethodField()
    image = SerializerMethodField()
    class Meta:
        model = Recipe
        fields = ['delete_url', 'id', 'user', 'title', 'image', 'body', 'mini_body', 'created_at', 'updated_at']

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.path
        except:
            image = None
        return image

class RecipeCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'body', 'mini_body', 'created_at', 'updated_at']
