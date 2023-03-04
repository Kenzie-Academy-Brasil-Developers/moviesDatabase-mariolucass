from .models import Movie
from rest_framework import serializers
from genres.serializers import GenreSerializer
from utils.movies_utils import MovieFields as MF
from utils.models_methods import genres_find_or_create


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Movie

        fields = MF.fields
        read_only_fields = MF.read_only_fields
        extra_kwargs = MF.extra_kwargs

    def create(self, validated_data) -> Movie:
        genres_data = validated_data.pop("genres")
        user_data = validated_data.pop("user")

        instance = Movie.objects.create(**validated_data, user=user_data)
        print(genres_data)

        genres = genres_find_or_create(genres_data)

        def sort_by_name(list):
            return list.name

        sorted_list = sorted(genres, key=sort_by_name)

        instance.genres.set(sorted_list)

        return instance
