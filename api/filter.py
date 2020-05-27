from django_filters.rest_framework import FilterSet, filters
from api.models import *


class BranchFilter(FilterSet):
    name = filters.CharFilter(method='branch_name_filter')

    class Meta:
        model = Branch
        fields = ['name']

    def branch_name_filter(self, queryset, name, value):
        name = self.request.query_params.get(name, None)
        if name is not None:
            queryset = queryset.filter(name__icontains=value)
        return queryset


class MovieFilter(FilterSet):
    title = filters.CharFilter(method='movie_title_filter')

    class Meta:
        model = Movie
        fields = ['title']

    def movie_title_filter(self, queryset, title, value):
        title = self.request.query_params.get(title, None)
        if title is not None:
            queryset = queryset.filter(title__icontains=value)
        return queryset



