from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('major', views.MajorViewSet)
router.register('student', views.StudentViewSet)
router.register('professor', views.ProfessorViewSet)
router.register('course', views.CourseViewSet)
router.register('basket', views.BasketViewSet)
router.register('registration', views.RegViewSet)

urlpatterns = [
    # path('major/', views.MajorList.as_view()),
    # path('major/<int:pk>/', views.MajorDetail.as_view()),
    # path('student/', views.StudentList.as_view()),
    # path('student/<int:pk>/', views.StudentDetail.as_view()),
    # path('professor/', views.ProfessorList.as_view()),
    # path('professor/<int:pk>/', views.ProfessorDetail.as_view()),
    # path('course/', views.CourseList.as_view()),
    # path('course/<int:pk>/', views.CourseDetail.as_view()),
    path('', include(router.urls))
]
