from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('major', views.MajorList)
router.register('student', views.StudentList)
router.register('professor', views.ProfessorList)
router.register('course', views.CourseList)
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
