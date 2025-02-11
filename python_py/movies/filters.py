import django_filters
from .models import Movie

class MovieFilter(django_filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            'title': ['icontains'],  # Filter by title (case-insensitive)
            'genre': ['icontains'],  # Filter by genre
            'release_year': ['exact', 'gte', 'lte'],  # Filter by release year
        }
