from .models import Movie
from django_filters.rest_framework import FilterSet

class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'movie_country': ['exact'],
            'movie_actor': ['exact'],
            'movie_date': ['gt', 'lt'],
            'movie_time': ['gt', 'lt']
        }