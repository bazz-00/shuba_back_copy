from rest_framework import routers
from django.urls import path

from .views import   UserViewSet

router = routers.DefaultRouter()
router.register("users", UserViewSet)

app_name = 'authentication'
urlpatterns = router.urls
