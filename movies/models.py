import uuid
from django.db import models
from users.models import User


class Movie(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=127)
    duration = models.DurationField()
    premiere = models.DateField()
    budget = models.DecimalField(decimal_places=2, max_digits=12)
    overview = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, related_name="movies", on_delete=models.CASCADE)
    genres = models.ManyToManyField("genres.Genre", related_name="movies")
