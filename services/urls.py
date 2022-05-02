from .views import ServiceTypeViewset, OrderServiceViewSet
from contacts.views import UserViewSet
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('services', ServiceTypeViewset)
router.register('orders', OrderServiceViewSet)
router.register('users', UserViewSet)

urlpatterns = router.urls
