from rest_framework import routers
from .api import OrderViewSet, OrderCommentsViewSet, OrderPhotosViewSet, SpecialityOrderViewSet

router = routers.DefaultRouter()
router.register('api/order', OrderViewSet, 'order')
router.register('api/specialityorder', SpecialityOrderViewSet, 'specialityorder')
router.register('api/order_comments', OrderCommentsViewSet, 'order_comments')
router.register('api/orderphotos', OrderPhotosViewSet, 'orderphotos')
urlpatterns = router.urls




