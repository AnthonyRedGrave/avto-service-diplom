from .serializers import UserSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return super().get_queryset().filter(is_superuser=False).order_by('first_name')


