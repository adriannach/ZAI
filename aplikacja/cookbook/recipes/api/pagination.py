from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
    )

class RecipeLimitOffsetPagination(LimitOffsetPagination):
    max_limit = 6
    default_limit = 6

class RecipePageNumberPagination(PageNumberPagination):
    page_size = 6
