from rest_framework.routers import DefaultRouter
from .views import OrderAPIView

router = DefaultRouter()
router.register('orders', OrderAPIView)

urlpatterns = router.urls
