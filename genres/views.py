from .models import Genre
from rest_framework import generics
from .serializers import GenreSerializer
from rest_framework.pagination import PageNumberPagination


class GenreView(generics.ListCreateAPIView):
    serializer_class = GenreSerializer
    pagination_class = PageNumberPagination
    queryset = Genre.objects.all()
