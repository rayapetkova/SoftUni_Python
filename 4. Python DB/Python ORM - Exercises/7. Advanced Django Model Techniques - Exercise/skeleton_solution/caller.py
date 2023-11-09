import os
import django
from _decimal import Decimal
from django.core.exceptions import ValidationError

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
# from main_app.models import FlashHero, SpiderHero
#
# Create queries within functions
# Create instance of SpiderHero
# spiderman = SpiderHero(name="Spider-Man", hero_title="Spider Hero", energy=100)
# # Create instance of FlashHero
# flash = FlashHero(name="The Flash", hero_title="Flash Hero", energy=70)
#
# # Save the instances to the database
# # spiderman.save()
# # flash.save()
#
# # Run the special abilities
# print(spiderman.swing_from_buildings())
# print(flash.run_at_super_speed())
# print(spiderman.swing_from_buildings())
#
# # Recharge the energy of Spider-Man and The Flash using the mixin method
# spiderman.recharge_energy(195)
# flash.recharge_energy(40)
#
# # Now you can check the updated energy levels
# print(f"{spiderman.name} - Energy: {spiderman.energy}")
# print(f"{flash.name} - Energy: {flash.energy}")
