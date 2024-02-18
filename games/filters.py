from django_filters import rest_framework as filters
from .models import Game, Studio


class GameFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr = "icontains")
    release_date__gt = filters.NumberFilter(field_name='year', lookup_expr='gte')
    release_date__lt = filters.NumberFilter(field_name='year', lookup_expr='lte')
    class Meta:
        model = Game
        fields = ['name', 'studio', 'year']
