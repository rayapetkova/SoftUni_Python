from django.core import validators
from django.db import models

from main_app.managers import CustomAuthorManager


class Author(models.Model):
    full_name = models.CharField(
        max_length=100,
        validators=[
            validators.MinLengthValidator(3),
            validators.MaxLengthValidator(100)
        ]
    )

    email = models.EmailField(
        unique=True
    )

    is_banned = models.BooleanField(
        default=False
    )

    birth_year = models.PositiveIntegerField(
        validators=[
            validators.MinValueValidator(1900),
            validators.MaxValueValidator(2005)
        ]
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    objects = CustomAuthorManager()


class Article(models.Model):

    CATEGORY_CHOICES = (
        ("Technology", "Technology"),
        ("Science", "Science"),
        ("Education", "Education")
    )

    title = models.CharField(
        max_length=200,
        validators=[
            validators.MinLengthValidator(5),
            validators.MaxLengthValidator(200)
        ]
    )

    content = models.TextField(
        validators=[
            validators.MinLengthValidator(10)
        ]
    )

    category = models.CharField(
        max_length=10,
        default="Technology",
        validators=[validators.MaxLengthValidator(10)],
        choices=CATEGORY_CHOICES
    )

    authors = models.ManyToManyField(
        to='Author',
        related_name='author_articles'
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )


class Review(models.Model):
    content = models.TextField(
        validators=[
            validators.MinLengthValidator(10)
        ]
    )

    rating = models.FloatField(
        validators=[
            validators.MinValueValidator(1.0),
            validators.MaxValueValidator(5.0)
        ]
    )

    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
        related_name='author_reviews'
    )

    article = models.ForeignKey(
        to='Article',
        on_delete=models.CASCADE,
        related_name='article_reviews'
    )

    published_on = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )