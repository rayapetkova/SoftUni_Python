import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
from main_app.models import Product


# Create and check models
def add_initial_products():
    # Adding the first product
    product1 = Product(
        name="Smartphone",
        description="A high-end smartphone with a powerful camera and fast processor.",
        price=799.99,
        category="Electronics",
        supplier="TechGadget Inc."
    )
    product1.save()

    # Adding the second product
    product2 = Product(
        name="Running Shoes",
        description="Comfortable running shoes with cushioned soles for long-distance runs.",
        price=79.99,
        category="Footwear",
        supplier="Sports Gear Co."
    )
    product2.save()

    # Adding the third product
    product3 = Product(
        name="Coffee Maker",
        price=149.95,
        category="Appliances",
        supplier="Kitchen Essentials Ltd."
    )
    product3.save()
    return "3 products were added successfully to the database"

def add_new_product_with_time_of_creation_and_edition():
    # Adding the first product
    product4 = Product(
        name="LED TV",
        description="A 55-inch LED TV with 4K resolution and smart TV capabilities.",
        price=699.99,
        category="Electronics",
        supplier="ElectroTech Inc."
    )
    product4.save()
    return "1 product with time of creation and edition was added to the database"

def add_products_with_count_value():
    product5 = Product(
        name="Laptop Bag",
        description="A stylish and durable laptop bag with multiple compartments.",
        price=49.95,
        category="Accessories",
        supplier="FashionStyle Co.",
        count=126
    )
    product5.save()

    product6 = Product(
        name="Stainless Steel Water Bottle",
        description="A 32 oz stainless steel water bottle with double-wall insulation.",
        price=19.99,
        category="Kitchenware",
        supplier="HealthyLiving Supplies"
    )
    product6.save()
    return "2 products with count were added to the database"


# Run and print your queries

# print(add_initial_products())

# print(add_new_product_with_time_of_creation_and_edition())

print(add_products_with_count_value())
