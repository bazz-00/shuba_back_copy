from rest_framework import routers
from .api import ExecutorViewSet, SpecialityViewSet, ExecutorCommentsViewSet

router = routers.DefaultRouter()
router.register('api/executor', ExecutorViewSet, 'executor')
router.register('api/speciality', SpecialityViewSet, 'speciality')
router.register('api/executor_comments', ExecutorCommentsViewSet, 'executor_comments')
urlpatterns = router.urls

