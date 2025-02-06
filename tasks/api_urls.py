from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet

# Register the API ViewSet with the router
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # This includes all the routes for your viewset
]
