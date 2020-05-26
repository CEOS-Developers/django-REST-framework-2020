from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('major', views.MajorView)
router.register('student', views.StudentView)
router.register('professor', views.ProfessorView)
router.register('course', views.CourseView)
router.register('registration', views.RegView)

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
