# Generated by Django 4.1 on 2023-03-04 03:17

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "stars",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MaxValueValidator(5),
                            django.core.validators.MinValueValidator(1),
                        ]
                    ),
                ),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(blank=True, default=False)),
            ],
            options={
                "ordering": ["id"],
            },
        ),
    ]