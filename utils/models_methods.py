from genres.models import Genre


def genres_find_or_create(genres_data):
    genres = []
    for genre in genres_data:
        genre, _ = Genre.objects.get_or_create(name=genre["name"])
        genres.append(genre)

    return genres
