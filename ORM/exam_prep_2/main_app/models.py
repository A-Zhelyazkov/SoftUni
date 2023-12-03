from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from main_app.managers import DirectorManager


class Person(models.Model):
    class Meta:
        abstract = True

    full_name = models.CharField(
        max_length=120,
        validators=[
            MinLengthValidator(2),
        ],
    )

    birth_date = models.DateField(
        default="1900-01-01",
    )

    nationality = models.CharField(
        max_length=50,
        default="Unknown",
    )


class Director(Person):
    years_of_experience = models.SmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0)
        ]
    )

    objects = DirectorManager()


class Actor(Person):
    is_awarded = models.BooleanField(
        default=False,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )


class Movie(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Other", "Other")
    ]

    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(5),
        ],
    )

    release_date = models.DateField()

    storyline = models.TextField(
        null=True,
        blank=True,
    )

    genre = models.CharField(
        max_length=6,
        choices=GENRE_CHOICES,
        default="Other",
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(10)
        ],
        default=0
    )

    is_classic = models.BooleanField(
        default=False,
    )

    is_awarded = models.BooleanField(
        default=False,
    )

    last_updated = models.DateTimeField(
        auto_now=True,
    )

    director = models.ForeignKey(
        to=Director,
        on_delete=models.CASCADE,
        related_name="movies"
    )

    starring_actor = models.ForeignKey(
        to=Actor,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="movies"
    )

    actors = models.ManyToManyField(
        to=Actor,
    )