from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import HjhgfjgViewSet

router = DefaultRouter()
router.register("hjhgfjg", HjhgfjgViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
