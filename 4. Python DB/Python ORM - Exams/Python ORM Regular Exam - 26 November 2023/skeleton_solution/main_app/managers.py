from django.db import models
from django.db.models import Count


class CustomAuthorManager(models.Manager):

    def get_authors_by_article_count(self):
        return self.annotate(total_articles=Count('author_articles'))\
            .order_by('-total_articles', 'email')
