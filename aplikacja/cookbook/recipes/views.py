from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Recipe
from .forms import RecipeForm

def recipe_index(request):
    recipes = Recipe.objects.all()

#    if request.user.is_authenticated:
 #       context = {
  #          'title': 'Index zalogowany'
   #     }
#    else:
 #       context = {
  #          'title': 'Index nie zalogowany'
   #     }
    context = {
        'recipes': recipes
    }
    return render(request, 'index.html', context)

def recipe_create(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.save()
        messages.success(request, "Dodano przepis")
        return HttpResponseRedirect(reverse('show', args=(recipe.id,)))
    context = {
        'form': form
    }
    return render(request, 'create.html', context)

def recipe_show(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)
    context = {
        'recipe': recipe
    }
    return render(request, 'show.html', context)

def recipe_update(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        recipe = form.save(commit=False)
        recipe.save()
        messages.success(request, "Edytowano post")
        return HttpResponseRedirect(reverse('show', args=(recipe.id,)))
    context = {
        'recipe': recipe,
        'form': form
    }
    return render(request, 'create.html', context)

def recipe_delete(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    messages.success(request, "Usunięto post")
    return redirect('index')