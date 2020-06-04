from django_filters.rest_framework import FilterSet, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import *


class WorkersFilter(FilterSet):  # workers filtered by gender
    gender = filters.CharFilter(method='filter_by_gender')

    class Meta:
        model = Workers
        fields = ['gender']

    def filter_by_gender(self, queryset, gender, value):
        return queryset.filter(**{
            gender: value,
        })
