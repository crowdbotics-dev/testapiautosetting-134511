from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134511ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134511", Testconnectors134511ViewSet, basename="testconnectors134511"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
