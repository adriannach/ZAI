from django.urls import path

from . import views

urlpatterns = [
    path('comments/delete/<int:id>/<int:idC>', views.comment_delete, name='comment_delete'),
    path('comments/create/<int:id>', views.comment_create, name='comment_create'),
    #path('<int:id>/delete/', views.recipe_delete, name='delete'),
]