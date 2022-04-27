from .views import ServiceTypeViewset
from rest_framework.routers import SimpleRouter


router = SimpleRouter()

router.register('services', ServiceTypeViewset)

urlpatterns = router.urls
