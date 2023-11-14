from _decimal import Decimal
from django.db import models
from django.db.models import Count, Max, Min, Avg


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        return self.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        return self.filter(price__range=(min_price, max_price))

    def with_bedrooms(self, bedrooms_count: int):
        return self.filter(bedrooms=bedrooms_count)

    def popular_locations(self):
        return self.values('location').annotate(total_visits=Count('location')).order_by('-total_visits')[:2]


class VideoGameManager(models.Manager):

    def games_by_genre(self, genre: str):
        return self.filter(genre=genre)

    def recently_released_games(self, year: int):
        return self.filter(release_year__gte=year)

    def highest_rated_game(self):
        highest_rated = self.aggregate(highest_rated_game=Max('rating'))['highest_rated_game']
        return self.filter(rating=highest_rated).first()

    def lowest_rated_game(self):
        lowest_rated = self.aggregate(lowest_rated_game=Min('rating'))['lowest_rated_game']
        return self.filter(rating=lowest_rated).first()

    def average_rating(self):
        average_rating = self.aggregate(average_rating=Avg('rating'))['average_rating']
        return f"{float(average_rating):.1f}"
