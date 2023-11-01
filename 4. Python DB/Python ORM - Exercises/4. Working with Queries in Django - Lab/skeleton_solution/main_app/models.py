from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    biography = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    genre = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    page_count = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Review(models.Model):
    reviewer_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    rating = models.PositiveIntegerField()
    comment = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return f"Review by {self.reviewer_name}"