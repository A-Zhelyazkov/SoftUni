import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Profile, Product, Order
from django.db.models import Q, Max, Count, F


def get_profiles(search_string=None):
    if search_string is None:
        return ""

    profiles = Profile.objects.filter(
        Q(full_name__icontains=search_string)
        |
        Q(email__icontains=search_string)
        |
        Q(phone_number__icontains=search_string)
    ).order_by("full_name")

    if not profiles:
        return ""

    result = []

    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, email: {profile.email}, "
                      f"phone number: {profile.phone_number}, orders: {profile.orders.count()}")

    return "\n".join(p for p in result)


def get_loyal_profiles():
    profiles = Profile.objects.get_regular_customers()

    if not profiles:
        return ""

    result = []

    for profile in profiles:
        result.append(f"Profile: {profile.full_name}, orders: {profile.orders.count()}")

    return "\n".join(p for p in result)


def get_last_sold_products():

    last_order = Order.objects.prefetch_related('products').last()

    if not last_order or not last_order.products.exists():
        return ""

    products = [product.name for product in last_order.products.all()]

    return f"Last sold products: {', '.join(products)}"


def get_top_products():
    products = Product.objects.annotate(times_sold=Count('order')).filter(
        times_sold__gt=0
    ).order_by('-times_sold', 'name')[:5]

    if not products:
        return ""

    result = []
    for prod in products:
        result.append(f"{prod.name}, sold {prod.times_sold} times")

    return "Top products:" + '\n' + '\n'.join(p for p in result)


def apply_discounts():
    orders = Order.objects.annotate(count_products=Count("products")).filter(
        count_products__gt=2,
        is_completed=False
    ).update(total_price=F('total_price')*0.9)

    return f"Discount applied to {orders} orders."


def complete_order():
    oldest_order = Order.objects.prefetch_related("products").filter(
        is_completed=False,
    ).order_by("creation_date").first()

    if not oldest_order:
        return ""

    for product in oldest_order.products.all():
        product.in_stock-=1

        if product.in_stock == 0:
            product.is_available = False

        product.save()

    oldest_order.is_completed = True
    oldest_order.save()

    return "Order has been completed!"
