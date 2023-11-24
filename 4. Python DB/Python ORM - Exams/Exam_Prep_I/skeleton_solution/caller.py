import os
import django
from django.db.models import Count, Avg, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Director, Actor, Movie


# Create and run your queries within functions
def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""

    all_directors = []

    if search_name is None:
        all_directors = Director.objects.filter(
            nationality__icontains=search_nationality
        ).order_by("full_name")

    elif search_nationality is None:
        all_directors = Director.objects.filter(
            full_name__icontains=search_name
        ).order_by("full_name")

    else:
        all_directors = Director.objects.filter(
            full_name__icontains=search_name,
            nationality__icontains=search_nationality
        ).order_by('full_name')

    if not all_directors:
        return ""

    final_result = []
    for director in all_directors:
        final_result.append(f"Director: {director.full_name}, nationality: {director.nationality}, "
                            f"experience: {director.years_of_experience}")

    return '\n'.join(final_result)


def get_top_director():
    top_director = Director.objects.get_directors_by_movies_count().first()

    if not top_director:
        return ''

    return f"Top Director: {top_director.full_name}, movies: {top_director.total_movies}."


def get_top_actor():
    top_actor = Actor.objects.annotate(
        total_starring_movies=Count('actor_starring_movies'),
        movies_avg_rating=Avg('actor_starring_movies__rating')
    ) \
        .order_by('-total_starring_movies', 'full_name') \
        .first()

    if not Movie.objects.all() or not top_actor:
        return ""

    top_actor_movies = ', '.join([m.title for m in top_actor.actor_starring_movies.all()])

    return f"Top Actor: {top_actor.full_name}, starring in movies: {top_actor_movies}, " \
           f"movies average rating: {top_actor.movies_avg_rating:.1f}"


def get_actors_by_movies_count():
    actors = Actor.objects.annotate(total_movies=Count('actor_all_movies'))\
        .order_by('-total_movies', 'full_name')[:3]

    if not Movie.objects.all() or not actors:
        return ""

    final_result = []
    for actor in actors:
        final_result.append(f"{actor.full_name}, participated in {actor.total_movies} movies")

    return '\n'.join(final_result)


def get_top_rated_awarded_movie():
    top_rated_movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()

    if not top_rated_movie:
        return ""

    starring_actor = top_rated_movie.starring_actor.full_name if top_rated_movie.starring_actor else 'N/A'
    participating_actors = ', '.join([a.full_name for a in top_rated_movie.actors.order_by('full_name')])

    return f"Top rated awarded movie: {top_rated_movie.title}, " \
           f"rating: {float(top_rated_movie.rating):.1f}. " \
           f"Starring actor: {starring_actor}. Cast: {participating_actors}."


def increase_rating():
    movies = Movie.objects.filter(
        is_classic=True,
        rating__lt=10
    )

    if not movies:
        return f"No ratings increased."

    updated_movies = movies.update(rating=F('rating') + 0.1)

    return f"Rating increased for {updated_movies} movies."










# DATA CREATION
# director1 = Director.objects.create(
#     full_name='First Director',
#     birth_date='1956-01-01',
#     nationality='Bulgarian',
#     years_of_experience=10
# )
#
# director2 = Director.objects.create(
#     full_name='Second Director',
#     birth_date='1960-01-01',
#     nationality='Romanian',
#     years_of_experience=5
# )
#
# director3 = Director.objects.create(
#     full_name='Third Director',
#     birth_date='1968-01-01',
#     nationality='Turkish',
#     years_of_experience=4
# )
#
# director4 = Director.objects.create(
#     full_name='Forth Director',
#     birth_date='1970-01-01',
#     nationality='French',
#     years_of_experience=6
# )
#
#
# actor1 = Actor.objects.create(
#     full_name='First Actor',
#     birth_date='1944-01-01',
#     nationality='Russian',
#     is_awarded=False,
# )
#
# actor2 = Actor.objects.create(
#     full_name='Second Actor',
#     birth_date='1935-01-01',
#     nationality='Bulgarian',
#     is_awarded=True,
# )
#
# actor3 = Actor.objects.create(
#     full_name='Third Actor',
#     birth_date='1968-01-01',
#     nationality='Romanian',
#     is_awarded=False,
# )
#
# actor4 = Actor.objects.create(
#     full_name='Forth Actor',
#     birth_date='1960-01-01',
#     nationality='Lithuanian',
#     is_awarded=True,
# )
#
#
# movie1 = Movie.objects.create(
#     title='First Movie',
#     release_date='2000-01-01',
#     storyline='First Storyline',
#     genre='Action',
#     rating=10,
#     is_classic=True,
#     is_awarded=True,
#     director=director1,
#     starring_actor=actor1,
# )
#
# # movie1.actors.add(actor1, actor2, actor3)
#
# movie2 = Movie.objects.create(
#     title='Second Movie',
#     release_date='2002-01-01',
#     storyline='Second Storyline',
#     genre='Comedy',
#     rating=6,
#     is_classic=False,
#     is_awarded=True,
#     director=director2,
#     starring_actor=actor2,
# )
#
# # movie2.actors.add(actor2, actor3, actor4)
#
# movie3 = Movie.objects.create(
#     title='Third Movie',
#     release_date='2005-01-01',
#     storyline='Third Storyline',
#     genre='Drama',
#     rating=8,
#     is_classic=True,
#     is_awarded=False,
#     director=director3,
#     starring_actor=actor3,
# )
#
# # movie3.actors.add(actor3, actor4, actor1)
#
# movie4 = Movie.objects.create(
#     title='Forth Movie',
#     release_date='2007-01-01',
#     storyline='Forth Storyline',
#     genre='Other',
#     rating=4,
#     is_classic=False,
#     is_awarded=False,
#     director=director4,
#     starring_actor=actor4,
# )
#
# # movie4.actors.add(actor4, actor1, actor2)