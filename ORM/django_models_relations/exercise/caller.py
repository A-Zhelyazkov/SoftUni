import os
from datetime import timedelta, date

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Author, Book, Artist, Song, Product, Review, DrivingLicense, Driver, Registration, Car, \
    Owner


def show_all_authors_with_their_books():
    authors = Author.objects.all().order_by("id")
    authors_with_books = []

    for author in authors:
        books = author.book_set.all()

        if books:
            titles = ', '.join(book.title for book in books)
        else:
            continue
        authors_with_books.append(f"{author.name} has written - {titles}!")

    return '\n'.join(str(a) for a in authors_with_books)


def delete_all_authors_without_books():
    Author.objects.filter(book__isnull=True).delete()


def add_song_to_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.add(song)


def get_songs_by_artist(artist_name):
    artist = Artist.objects.get(name=artist_name)

    return artist.songs.order_by("-id")


def remove_song_from_artist(artist_name, song_title):
    artist = Artist.objects.get(name=artist_name)
    song = Song.objects.get(title=song_title)

    artist.songs.remove(song)


def calculate_average_rating_for_product_by_name(product_name):
    product = Product.objects.get(name=product_name)
    reviews = product.reviews.all()
    total_rating = 0

    for review in reviews:
        total_rating += review.rating
    average_rating = total_rating / len(reviews)

    return average_rating


def get_reviews_with_high_ratings(threshold):
    return Review.objects.filter(rating__gte=threshold)


def get_products_with_no_reviews():
    return Product.objects.filter(reviews__isnull=True).order_by('-name')


def delete_products_without_reviews():
    Product.objects.filter(review__isnull=True).delete()


def calculate_licenses_expiration_dates():
    licenses = DrivingLicense.objects.order_by("-license_number")

    return '\n'.join(str(l) for l in licenses)


def get_drivers_with_expired_licenses(due_date):
    modified_date = due_date - timedelta(days=365)

    return Driver.objects.filter(drivinglicense__issue_date__gt=modified_date)


def register_car_by_owner(owner):
    registration = Registration.objects.filter(car__isnull=True).first()
    car = Car.objects.filter(registration__isnull=True, owner=owner).first()

    car.owner = owner
    car.registration = registration
    car.save()

    registration.registration_date = date.today()
    registration.car = car
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."
