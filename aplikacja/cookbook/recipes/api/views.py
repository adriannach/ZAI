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

class RecipeIndexAPIView(ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeIndexSerializer

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