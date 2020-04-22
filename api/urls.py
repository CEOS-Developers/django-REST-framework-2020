from django.conf.urls import url
from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/<int:pk>/', views.UserDetail.as_view()),
    path('branch/', views.BranchListCreate.as_view()),
    path('branch/<int:pk>/', views.BranchDetail.as_view()),
    path('screen/', views.ScreenListCreate.as_view()),
    path('movie/', views.MovieListCreate.as_view()),
    path('movie/<int:pk>/', views.MovieDetail.as_view()),
    path('schedule/', views.ScheduleListCreate.as_view()),
    path('schedule/<int:pk>/', views.ScheduleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
