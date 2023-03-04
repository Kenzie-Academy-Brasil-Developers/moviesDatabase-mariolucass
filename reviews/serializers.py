from .models import Review
from users.models import User
from rest_framework import serializers
from utils.reviews_utils import ReviewFields as RF
from utils.user_utils import CriticFields as CF


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = CF.fields
        read_only_fields = CF.read_only_fields
        extra_kwargs = CF.extra_kwargs


class ReviewSerializer(serializers.ModelSerializer):
    critic = CriticSerializer(required=False)

    class Meta:
        model = Review

        fields = RF.fields
        read_only_fields = RF.read_only_fields
        extra_kwargs = RF.extra_kwargs

    movie_id = serializers.SerializerMethodField()

    def get_movie_id(self, obj):
        return obj.movie.id
