from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CommentForm
from .models import Comment
from django.contrib import messages
from django.urls import reverse
# Create your views here.
from recipes.models import Recipe


def comment_create(request, id=None):
    recipe = get_object_or_404(Recipe, id=id)

    if not request.user.is_authenticated:
        messages.success(request, "Zaloguj się aby dodać komentarz")
        raise Http404

    form_comment = CommentForm(request.POST or None)
    if form_comment.is_valid():
        comment = form_comment.save(commit=False)
        comment.user = request.user
        comment.recipe = recipe
        comment.save()

        messages.success(request, "Dodano komentarz")

        return HttpResponseRedirect(reverse('show', args=(recipe.id,)))

def comment_delete(request, id, idC):
    recipe_id = id
    comment = get_object_or_404(Comment, id=idC)

    if comment.user != request.user:
        messages.success(request, "Nie jesteś twórcą komentarza")
        raise Http404

    comment.delete()
    messages.success(request, "Usunięto komentarz")
    return HttpResponseRedirect(reverse('show', args=(recipe_id,)))