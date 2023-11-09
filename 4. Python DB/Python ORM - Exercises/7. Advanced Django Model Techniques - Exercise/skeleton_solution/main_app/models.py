from django.core.exceptions import ValidationError
from django.db import models
from django.core import validators


def validate_name(value: str):
    for el in value:
        if not el.isalpha() and not el.isspace():
            raise ValidationError(message="Name can only contain letters and spaces")

    return value


def validate_age(value):
    if value < 18:
        raise ValidationError(message="Age must be greater than 18")

    return value


def validate_phone_number(value: str):
    if not (value.startswith("+359") and len(value) == 14 and value[4:].isdigit()):
        raise ValidationError(message="Phone number must start with a '+359' followed by 9 digits")

    return value


class RechargeEnergyMixin:

    def recharge_energy(self, amount: int):
        self.energy = min(self.energy + amount, 100)
        self.save()


class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[validators.RegexValidator(regex=r"[A-Za-z\s]+",
                                   message="Name can only contain letters and spaces"
                                   )]
    )

    age = models.PositiveIntegerField(
        validators=[validate_age]
    )

    email = models.EmailField(
        error_messages={
            'invalid': "Enter a valid email address"
        }
    )

    phone_number = models.CharField(
        max_length=13,
        validators=[validators.RegexValidator(regex=r"^\+359\d{9}$",
                                   message="Phone number must start with a '+359' followed by 9 digits"
                                   )]
    )

    website_url = models.URLField(
        error_messages={
            'invalid': "Enter a valid URL"
        }
    )


class BaseMedia(models.Model):

    class Meta:
        abstract = True
        ordering = ['-created_at', 'title']

    title = models.CharField(
        max_length=100
    )

    description = models.TextField()

    genre = models.CharField(
        max_length=50
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Book(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Book'
        verbose_name_plural = 'Models of type - Book'

    author = models.CharField(
        max_length=100,
        validators=[validators.MinLengthValidator(
            limit_value=5,
            message=f"Author must be at least 5 characters long"
        )]
    )

    isbn = models.CharField(
        max_length=20,
        unique=True,
        validators=[validators.MinLengthValidator(
            limit_value=6,
            message=f"ISBN must be at least 6 characters long"
        )]
    )


class Movie(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Movie'
        verbose_name_plural = 'Models of type - Movie'

    director = models.CharField(
        max_length=100,
        validators=[validators.MinLengthValidator(
            limit_value=8,
            message=f"Director must be at least 8 characters long"
        )]
    )


class Music(BaseMedia):

    class Meta(BaseMedia.Meta):
        verbose_name = 'Model Music'
        verbose_name_plural = 'Models of type - Music'

    artist = models.CharField(
        max_length=100,
        validators=[validators.MinLengthValidator(
            limit_value=9,
            message="Artist must be at least 9 characters long"
        )]
    )


class Product(models.Model):
    name = models.CharField(
        max_length=100
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def calculate_tax(self):
        tax = (8/100) * float(self.price)
        return tax

    def calculate_shipping_cost(self, weight):
        shipping_cost = float(weight) * 2.00
        return shipping_cost

    def format_product_name(self):
        return f"Product: {self.name}"


class DiscountedProduct(Product):

    class Meta:
        proxy = True

    def calculate_price_without_discount(self):
        price_without_discount = (20/100) * float(self.price) + float(self.price)
        return price_without_discount

    def calculate_tax(self):
        tax = (5/100) * float(self.price)
        return tax

    def calculate_shipping_cost(self, weight):
        shipping_cost = float(weight) * 1.50
        return shipping_cost

    def format_product_name(self):
        return f"Discounted Product: {self.name}"


class Hero(models.Model, RechargeEnergyMixin):
    name = models.CharField(
        max_length=100
    )

    hero_title = models.CharField(
        max_length=100
    )

    energy = models.PositiveIntegerField()


class SpiderHero(Hero):

    class Meta:
        proxy = True

    def swing_from_buildings(self):
        self.energy -= 80

        if self.energy <= 0:
            return f"{self.name} as Spider Hero is out of web shooter fluid"

        self.save()
        return f"{self.name} as Spider Hero swings from buildings using web shooters"


class FlashHero(Hero):

    class Meta:
        proxy = True

    def run_at_super_speed(self):
        self.energy -= 65

        if self.energy <= 0:
            return f"{self.name} as Flash Hero needs to recharge the speed force"

        self.save()
        return f"{self.name} as Flash Hero runs at lightning speed, saving the day"
