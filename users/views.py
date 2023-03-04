from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from utils.authorizations import AdminPermissions
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [AdminPermissions()]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
