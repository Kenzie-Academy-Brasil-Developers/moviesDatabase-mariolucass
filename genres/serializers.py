from .models import Genre
from rest_framework import serializers
from utils.genres_utils import GenreFields as GF


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = GF.fields
        read_only_fields = GF.read_only_fields
        extra_kwargs = GF.extra_kwargs
