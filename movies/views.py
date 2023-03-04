from .models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from utils.authorizations import AdminOrReadOnlyPermissions
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class MovieView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [AdminOrReadOnlyPermissions]

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
