import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order
from django.db.models import Q, Count, F


# Create and run your queries within functions
def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.annotate(total_orders=Count('profile_orders')) \
        .filter(Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(
        phone_number__icontains=search_string)
                ).order_by('full_name')

    if not profiles:
        return ""

    final_result = []
    for profile in profiles:
        final_result.append(f"Profile: {profile.full_name}, "
                            f"email: {profile.email}, "
                            f"phone number: {profile.phone_number}, "
                            f"orders: {profile.total_orders}")

    return '\n'.join(final_result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    final_result = []
    for profile in profiles:
        final_result.append(f"Profile: {profile.full_name}, orders: {profile.total_orders}")

    return '\n'.join(final_result)


def get_last_sold_products():
    last_order = Order.objects.last()

    if not Order.objects.all() or not last_order.products.all():
        return ""

    return f"Last sold products: {', '.join([p.name for p in last_order.products.order_by('name')])}"


def get_top_products():
    products = Product.objects.annotate(total_orders_sold=Count('product_orders')) \
                   .filter(total_orders_sold__gt=0) \
                   .order_by('-total_orders_sold', 'name')[:5]

    if not Order.objects.all() or not products:
        return ""

    final_result = ['Top products:']
    for product in products:
        final_result.append(f"{product.name}, sold {product.total_orders_sold} times")

    return '\n'.join(final_result)


def apply_discounts():
    orders = Order.objects.annotate(total_products=Count('products')) \
        .filter(total_products__gt=2, is_completed=False)

    updated_orders = 0
    if orders:
        updated_orders = orders.update(total_price=F('total_price') - (10 / 100) * F('total_price'))

    return f"Discount applied to {updated_orders} orders."

def complete_order():
    order = Order.objects.filter(
        is_completed=False
    ).first()

    if not Order.objects.all() or not order:
        return ""

    for product in order.products.all():
        if product.is_available:
            product.in_stock -= 1

            if product.in_stock == 0:
                product.is_available = False

            product.save()

    order.is_completed = True
    order.save()

    return f"Order has been completed!"
