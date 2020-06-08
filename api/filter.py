from django_filters.rest_framework import FilterSet, filters
from api.models import *


class WeekdayFilter(FilterSet):
    weekday = filters.CharFilter(method='course_day_filter')

    class Meta:
        model = Course
        fields = ['weekday']

    def course_day_filter(self):
        queryset = Course.objects.all()
        weekday = self.request.query_params.get('weekday', None)

        if weekday is not None:
            queryset = queryset.filter(weekday=weekday)
        return queryset


class CreditFilter(FilterSet):
    credit = filters.NumberFilter(method='course_credit_filter')

    class Meta:
        model = Course
        fields = ['credit']

    def course_credit_filter(self):
        queryset = Course.objects.all()
        credit = self.request.query_params.get('credit', None)

        if credit is not None:
            queryset = queryset.filter(credit=credit)
        return queryset
