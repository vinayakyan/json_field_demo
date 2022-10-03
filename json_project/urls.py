from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from json_app.views import EmployeeViewSet

router = DefaultRouter()
router.register('emp', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
