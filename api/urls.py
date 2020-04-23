from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'branch', BranchViewSet)
router.register(r'screen', ScreenViewSet)
router.register(r'movie', MovieViewSet)
router.register(r'schedule', ScheduleViewSet)
urlpatterns = router.urls
