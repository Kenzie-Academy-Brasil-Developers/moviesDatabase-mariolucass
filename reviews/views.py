from .models import Review
from movies.models import Movie
from rest_framework import generics
from .serializers import ReviewSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from utils.authorizations import AdminOrCriticOrReadOnlyPermissions
from rest_framework_simplejwt.authentication import JWTAuthentication


class ReviewView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrCriticOrReadOnlyPermissions]

    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_url_kwarg = "movie_id"

    def get_queryset(self):
        movie_id = self.kwargs.get("movie_id")
        movie = get_object_or_404(Movie, id=movie_id)

        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        user = self.request.user

        movie_id = self.kwargs.get("movie_id")
        movie = get_object_or_404(Movie, id=movie_id)

        serializer.save(movie=movie, critic=user)
