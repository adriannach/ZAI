from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, UpdateAPIView,
    DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView )
from recipes.models import Recipe
from .serializers import (
    RecipeIndexSerializer, RecipeShowSerializer,
    RecipeCreateUpdateSerializer)
from rest_framework.permissions import (
AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
)
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

from .pagination import RecipeLimitOffsetPagination, RecipePageNumberPagination


class RecipeIndexAPIView(ListAPIView):
    serializer_class = RecipeIndexSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'body']
    pagination_class = RecipePageNumberPagination

    def get_queryset(self, *args, **kwargs):
        recipes = Recipe.objects.all()
        query = self.request.GET.get("q")
        if query:
            recipes = recipes.filter(Q(title__icontains=query) |
                                     Q(body__icontains=query)
                                     ).distinct()
        return recipes

class RecipeShowApiView(RetrieveAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeShowSerializer

class RecipeCreateApiView(CreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RecipeUpdateApiView(RetrieveUpdateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeCreateUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class RecipeDeleteApiView(DestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeShowSerializer