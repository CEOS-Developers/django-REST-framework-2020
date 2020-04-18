from django.conf.urls import url, include
from django.contrib import admin
# views 에서 작성한 ViewSet 을 Router 에 연결하면 url 을 자동으로 매핑해준다. (DRF 의 router)
from rest_framework import routers
from api.views import MyUserViewSet

router = routers.DefaultRouter()
router.register(r'myusers', MyUserViewSet)   # prefix = myusers, viewset = MyUserViewSet

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]




'''
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
'''