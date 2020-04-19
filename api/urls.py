from django.urls import include,path
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('major', views.MajorList)
router.register('student', views.StudentList)
router.register('professor', views.ProfessorList)
router.register('course', views.CourseList)

urlpatterns = [
    path('', router.urls),
]
