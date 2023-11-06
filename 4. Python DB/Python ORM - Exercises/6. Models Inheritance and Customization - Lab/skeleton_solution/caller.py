import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# from datetime import date, timedelta
# from main_app.models import Mammal, Reptile

# Create and check models


# Run and print your queries
# lion_birth_date = date.today() - timedelta(days=731)
# lion = Mammal.objects.create(name="Simba", species="Lion", birth_date=lion_birth_date, sound="Roar", fur_color="Golden")
# print(f"The lion's age is {lion.age}.")
#
# snake_birth_date = date.today() - timedelta(days=30)
# snake = Reptile.objects.create(name="Kaa", species="Python", birth_date=snake_birth_date, sound="Hiss", scale_type="Scales")
# print(f"The snake's age is {snake.age}.")