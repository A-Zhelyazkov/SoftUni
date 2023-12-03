import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from django.db.models import Q

from main_app.models import Director, Actor, Movie
from populate_db import populate_model_with_data


def get_directors(search_name=None, search_nationality=None):
    if search_name is None and search_nationality is None:
        return ""
    query = None

    if search_name is None:
        query = Q(nationality__icontains=search_nationality)
    if search_nationality is None:
        query = Q(full_name__icontains=search_name)
    else:
        query = Q(nationality__icontains=search_nationality) & Q(full_name__icontains=search_name)

    directors = Director.objects.filter(query).order_by('full_name')
    result = []

    for director in directors:
        result.append(f"Director: {director.full_name}, nationality: {director.nationality}, "
                      f"experience: {director.years_of_experience}")

    return '\n'.join(result)


#next is get_top_director()