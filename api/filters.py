from django_filters.rest_framework import FilterSet, filters
from api.models import Review, User, Movie


class UserFilter(FilterSet):
    class Meta:
        model = User
        fields = ['gender']

    # users /?gender = 0,1,2
    def gender_filter(self, queryset, name, value):
        gender_queryset = queryset.filter(gender=value)
        return gender_queryset


class ReviewFilter(FilterSet):
    # reviews/?comment=value
    comment = filters.CharFilter(method='comments_filter')

    class Meta:
        model = Review
        fields = ['comment']

    # 'value'가 들어간 comment 필터링
    def comments_filter(self, queryset, comment, value):
        comment = self.request.query_params.get(comment, None)
        if comment is not None:
            queryset = queryset.filter(comment__icontains=value)
        return queryset


class MovieFilter(FilterSet):
    # movies/?title=value
    title = filters.CharFilter(method='movie_title_filter')

    class Meta:
        model = Movie
        fields = ['title']

    def movie_title_filter(self, queryset, title, value):
        title = self.request.query_params.get(title, None)
        if title is not None:
            queryset = queryset.filter(title__icontains=value)
        return queryset
