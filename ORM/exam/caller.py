import os
import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q, Count, Avg, Max
from main_app.models import Author, Review, Article


def get_authors(search_name=None, search_email=None):
    if search_email is None and search_name is None:
        return ""

    query = None

    if not search_email:
        query = Q(full_name__icontains=search_name)
    elif not search_name:
        query = Q(email__icontains=search_email)
    else:
        query = Q(email__icontains=search_email) & Q(full_name__icontains=search_name)

    authors = Author.objects.filter(query).order_by('-full_name')

    result = []

    for author in authors:
        status = None
        if author.is_banned:
            status = "Banned"
        else:
            status = "Not Banned"
        result.append(f"Author: {author.full_name}, email: {author.email}, status: {status}")

    return '\n'.join(result)


def get_top_publisher():
    top_author = Author.objects.get_authors_by_article_count().first()

    if not top_author or top_author.number_articles == 0:
        return ""

    return f"Top Author: {top_author.full_name} with {top_author.number_articles} published articles."


def get_top_reviewer():
    top_reviewer = (Author.objects.annotate(number_reviews=Count("reviews")).
                    order_by("-number_reviews", 'email')).first()

    if not top_reviewer or top_reviewer.number_reviews == 0:
        return ""

    return f"Top Reviewer: {top_reviewer.full_name} with {top_reviewer.number_reviews} published reviews."


def get_latest_article():
    last_article = Article.objects.annotate(avg_reviews_rating=Avg('reviews__rating', default=0),
                                              num_reviews=Count('reviews')).order_by('-published_on').first()

    if last_article:
        authors_names = sorted(author.full_name for author in last_article.authors.all())
        return (f"The latest article is: {last_article.title}. "
            f"Authors: {', '.join(authors_names)}. Reviewed: {last_article.reviews.count()} times. "
            f"Average Rating: {last_article.avg_reviews_rating:.2f}.")
    else:
        return ""

def get_top_rated_article():
    top_article = Article.objects.annotate(avg_rating=Avg('reviews__rating'),
                                           num_reviews=Count('reviews')).filter(num_reviews__gt=0).order_by('-avg_rating', 'title').first()

    if top_article:
        formatted_rating = "{:.2f}".format(top_article.avg_rating)
        result_string = f"The top-rated article is: {top_article.title}, with an average rating of {formatted_rating}, reviewed {top_article.num_reviews} times."
    else:
        result_string = ""

    return result_string


def ban_author(email=None):
    if email is None:
        return "No authors banned."

    author = Author.objects.filter(email=email).first()

    if not author:
        return "No authors banned."

    count_reviews = author.reviews.all().count()
    author.reviews.all().delete()
    author.is_banned = True
    author.save()

    return f"Author: {author.full_name} is banned! {count_reviews} reviews deleted."


