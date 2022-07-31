from rest_framework import routers
from contact.api import ContactViewSet


router = routers.DefaultRouter()
router.register('api/contact', ContactViewSet, 'contact')
urlpatterns = router.urls