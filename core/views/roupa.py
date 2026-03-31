from rest_framework.viewsets import ModelViewSet

from core.models import Roupa
from core.serializers import RoupaSerializer


class RoupaViewSet(ModelViewSet):
    queryset = Roupa.objects.all()
    serializer_class = RoupaSerializer
