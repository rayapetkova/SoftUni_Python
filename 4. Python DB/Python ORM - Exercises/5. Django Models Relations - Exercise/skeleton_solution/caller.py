import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Author, Book, \
    Song, Artist, \
    Product, Review, \
    Driver, DrivingLicense, \
    Owner, Car, Registration
from datetime import timedelta, date

# Create queries within functions
def show_all_authors_with_their_books():
    authors = Author.objects.all()

    final_result = []
    for author in authors:
        author_books = author.book_set.all()

        if author_books:
            final_result.append(f"{author.name} has written - {', '.join(b.title for b in author_books)}!")

    return '\n'.join(final_result)


def delete_all_authors_without_books():
    authors = Author.objects.all()

    for author in authors:
        if author.book_set.all().count() == 0:
            author.delete()


def add_song_to_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name: str):
    artist = Artist.objects.get(name=artist_name)
    return artist.songs.all().order_by("-id")


def remove_song_from_artist(artist_name: str, song_title: str):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name: str):
    product = Product.objects.filter(name=product_name).get()
    product_reviews = product.reviews.all()

    if product_reviews:
        return sum([r.rating for r in product_reviews]) / len(product_reviews)


def get_reviews_with_high_ratings(threshold: int):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by("-name")


def delete_products_without_reviews():
    Product.objects.filter(reviews__isnull=True).delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.all()

    final_result = []
    for license in licenses:
        expiration_date = license.issue_date + timedelta(days=365)

        final_result.append(f"License with id: {license.license_number} expires on {expiration_date}!")

    return '\n'.join(sorted(final_result, reverse=True))


def get_drivers_with_expired_licenses(due_date):
    licenses = DrivingLicense.objects.all()

    final_result_drivers = []
    for license in licenses:
        expiration_date = license.issue_date + timedelta(days=365)

        if expiration_date > due_date:
            final_result_drivers.append(license.driver)

    return final_result_drivers


def register_car_by_owner(owner: Owner):
    registration_not_related_to_car = Registration.objects.filter(car__isnull=True).first()
    car_without_registration = Car.objects.filter(registration__isnull=True).first()

    if registration_not_related_to_car and car_without_registration:
        car_without_registration.registration = registration_not_related_to_car
        registration_not_related_to_car.registration_date = date.today()

        car_without_registration.save()
        registration_not_related_to_car.save()

        return f"Successfully registered {car_without_registration.model} to {owner.name} with registration " \
               f"number {registration_not_related_to_car.registration_number}."
