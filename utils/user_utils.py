class UserFields:
    fields = [
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "bio",
        "password",
        "is_critic",
        "is_superuser",
        "updated_at",
    ]
    read_only_fields = ["id", "is_superuser", "updated_at"]
    extra_kwargs = {"password": {"write_only": True}}


class CriticFields:
    fields = ["id", "first_name", "last_name"]
    read_only_fields = ["id", "first_name", "last_name"]
    extra_kwargs = {}
