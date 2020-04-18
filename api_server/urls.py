from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
