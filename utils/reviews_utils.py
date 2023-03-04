class ReviewFields:
    fields = ["id", "stars", "review", "spoilers", "movie_id", "critic"]
    read_only_fields = ["id"]
    extra_kwargs = {"critic": {"required": False}}
