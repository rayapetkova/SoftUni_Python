import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Article, Review
from django.db.models import Count, Avg, Sum


# Create and run your queries within functions
def get_authors(search_name=None, search_email=None):

    if search_name is None and search_email is None:
        return ""

    authors = []

    if search_name is not None and search_email is not None:
        authors = Author.objects.filter(
            full_name__icontains=search_name,
            email__icontains=search_email
        ).order_by('-full_name')

    elif search_name is not None and search_email is None:
        authors = Author.objects.filter(
            full_name__icontains=search_name
        ).order_by('-full_name')

    elif search_name is None and search_email is not None:
        authors = Author.objects.filter(
            email__icontains=search_email
        ).order_by('-full_name')

    if not authors:
        return ""

    final_result = []
    for author in authors:
        status = ""

        if author.is_banned:
            status = "Banned"
        else:
            status = "Not Banned"

        final_result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return '\n'.join(final_result)


def get_top_publisher():
    top_author = Author.objects.annotate(total_articles=Count('author_articles'))\
        .filter(total_articles__gt=0)\
        .order_by('-total_articles', 'email')\
        .first()

    if not top_author:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.total_articles} published articles."


def get_top_reviewer():
    author = Author.objects.annotate(total_reviews=Count('author_reviews'))\
        .filter(total_reviews__gt=0)\
        .order_by('-total_reviews', 'email')\
        .first()

    if not author:
        return ""

    return f"Top Reviewer: {author.full_name} with {author.total_reviews} published reviews."


def get_latest_article():
    article = Article.objects.annotate(
        total_reviews=Count('article_reviews'),
        sum_ratings=Sum('article_reviews__rating')
    ).last()

    if not Article.objects.all():
        return ""

    article_authors = ', '.join([au.full_name for au in article.authors.order_by('full_name')])

    if article.total_reviews == 0:
        c_rating = 0
    else:
        c_rating = article.sum_ratings / article.total_reviews
    return f"The latest article is: {article.title}. Authors: {article_authors}. Reviewed: {article.total_reviews} times. Average Rating: {c_rating:.2f}."


def get_top_rated_article():
    article = Article.objects.annotate(
        total_reviews=Count('article_reviews'),
        avg_rating=Avg('article_reviews__rating')
    ).order_by('-avg_rating', 'title').first()

    if not Review.objects.all():
        return ""

    return f"The top-rated article is: {article.title}, with an average rating of {article.avg_rating:.2f}, " \
           f"reviewed {article.total_reviews} times."


def ban_author(email=None):

    if email is None:
        return f"No authors banned."

    author = Author.objects.filter(
        email__exact=email
    ).annotate(total_reviews=Count('author_reviews'))\
        .first()

    if not Author.objects.all() or not author:
        return f"No authors banned."

    author.is_banned = True
    author.save()

    message = f"Author: {author.full_name} is banned! {author.total_reviews} reviews deleted."

    for review in author.author_reviews.all():
        Review.objects.get(id=review.id).delete()

    return message


# print(get_latest_article())



# author1 = Author.objects.create(
#     full_name="First Author",
#     email="first@hotmail.com",
#     is_banned=False,
#     birth_year=1999
# )
#
# author2 = Author.objects.create(
#     full_name="Second Author",
#     email="second@hotmail.com",
#     is_banned=False,
#     birth_year=1995
# )
#
# article1 = Article.objects.create(
#     title="First Article",
#     content='idkkkkkkkkkkkkkkkkkkkkkkkkk',
#     category='Science'
# )
#
# article1.authors.add(author1)
#
# article2 = Article.objects.create(
#     title="Second Article",
#     content='idkkkkkkkkkkk222222222222222222',
# )
#
# article2.authors.add(author1, author2)
#
# review1 = Review.objects.create(
#     content='firstttttttttttttttttttttttt',
#     rating=4.9,
#     author=author1,
#     article=article1
# )
#
# review2 = Review.objects.create(
#     content='seconddddddddddddddddddddddddd',
#     rating=3.1,
#     author=author2,
#     article=article2
# )
