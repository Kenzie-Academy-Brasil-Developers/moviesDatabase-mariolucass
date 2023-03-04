import uuid
from django.db import models
from users.models import User
from movies.models import Movie
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    class Meta:
        ordering = ["id"]

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    stars = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    review = models.TextField()
    spoilers = models.BooleanField(default=False, blank=True)
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)
    critic = models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
