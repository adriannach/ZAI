from django.urls import path

from . import views

urlpatterns = [
    path('', views.recipe_index, name='index'),
    path('create/', views.recipe_create, name='create'),
    path('<int:id>/', views.recipe_show, name='show'),
    path('<int:id>/edit/', views.recipe_update, name='update'),
    path('<int:id>/delete/', views.recipe_delete, name='delete'),
]