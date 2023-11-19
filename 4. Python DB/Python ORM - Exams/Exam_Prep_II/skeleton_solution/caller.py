import os
import django
from django.db.models import Q, Count, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Profile, Product, Order


# Create and run your queries within functions

def get_profiles(search_string=None):
    searched_profiles = ''

    if not search_string:
        return ""

    searched_profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string) | Q(email__icontains=search_string) | Q(
            phone_number__icontains=search_string)
    ).annotate(num_orders=Count('profile_orders')).order_by('full_name')

    if not searched_profiles:
        return ""

    final_result = []
    for profile in searched_profiles:
        final_result.append(f"Profile: {profile.full_name}, email: {profile.email}, "
                            f"phone number: {profile.phone_number}, orders: {profile.num_orders}")

    return '\n'.join(final_result)


def get_loyal_profiles():
    loyal_profiles = Profile.objects.get_regular_customers()

    if not loyal_profiles:
        return ""

    final_result = []
    for profile in loyal_profiles:
        final_result.append(f"Profile: {profile.full_name}, orders: {profile.total_orders}")

    return '\n'.join(final_result)


def get_last_sold_products():
    last_order = Order.objects.last()

    if not Order.objects.all() or not last_order.products.all():
        return ""

    last_order_products = ', '.join([p.name for p in last_order.products.order_by('name')])

    return f"Last sold products: {last_order_products}"


def get_top_products():
    top_products = Product.objects \
                       .annotate(total_orders=Count('product_orders')) \
                       .filter(total_orders__gt=0) \
                       .order_by('-total_orders', 'name')[:5]

    if not Order.objects.all() or not top_products:
        return ""

    final_result = ['Top products:']
    for product in top_products:
        final_result.append(f"{product.name}, sold {product.total_orders} times")

    return '\n'.join(final_result)


def apply_discounts():
    order_objects = Order.objects.annotate(total_products=Count('products')) \
        .filter(total_products__gt=2, is_completed=False)

    updated_objects = order_objects.update(total_price=F('total_price') - 10 / 100 * F('total_price'))

    return f"Discount applied to {updated_objects} orders."


def complete_order():
    first_order = Order.objects.filter(is_completed=False).first()

    if not Order.objects.all() or not first_order:
        return ""

    for product in first_order.products.all():
        if product.is_available:
            product.in_stock -= 1

            if product.in_stock == 0:
                product.is_available = False

            product.save()

    first_order.is_completed = True
    first_order.save()

    return f"Order has been completed!"
