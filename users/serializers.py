from .models import User
from rest_framework import serializers
from utils.user_utils import UserFields as UF


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = UF.fields
        read_only_fields = UF.read_only_fields
        extra_kwargs = UF.extra_kwargs

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)
