from django.urls import path

from . import views

urlpatterns = [
    path('api/', views.RecipeIndexAPIView.as_view(), name='index_api'),
    path('api/create/', views.RecipeCreateApiView.as_view(), name='create_api'),
    path('api/<int:pk>/', views.RecipeShowApiView.as_view(), name='show_api'),
    path('api/<int:pk>/edit/', views.RecipeUpdateApiView.as_view(), name='update_api'),
    path('api/<int:pk>/delete/', views.RecipeDeleteApiView.as_view(), name='delete_api'),
]