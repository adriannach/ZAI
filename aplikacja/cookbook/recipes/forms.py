from ckeditor.widgets import CKEditorWidget
from django.forms import ModelForm, forms

from .models import Recipe
from django import forms


class RecipeForm(forms.ModelForm):
    title = forms.CharField(
        label = "Tytuł",
        max_length = 100,
        required = True,
    )

    image = forms.FileField(
        label = "Zdjęcie",
        required = False,
    )

    body = forms.CharField(
        label = "Przepis",
        widget = CKEditorWidget(),
        required=False,
    )

    mini_body = forms.CharField(
        label = "Krótki opis (widoczny na stronie głownej)",
        required = False,
        widget=forms.Textarea(attrs={"rows": 3}),
    )

    class Meta:
        model = Recipe
        fields = ['title', 'image', 'body', 'mini_body']
