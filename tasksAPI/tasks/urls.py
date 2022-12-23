from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . views import CollectionViewSet, TaskViewSet

router = DefaultRouter()
router.register("collections",viewset=CollectionViewSet, basename="collections")
router.register("task", viewset=TaskViewSet, basename="tasks")

urlpatterns = []
urlpatterns += router.urls
