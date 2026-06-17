from rest_framework.viewsets import ModelViewSet

from core.models import Roupa
from core.serializers.roupa import (
    RoupaCreateSerializer,
    RoupaRetrieveSerializer,
    RoupaSerializer,
)


class RoupaViewSet(ModelViewSet):
    queryset = Roupa.objects.all()

    def get_serializer_class(self):
        if self.action in ["retrieve", "list"]:
            return RoupaRetrieveSerializer

        if self.action in ["create", "update", "partial_update"]:
            return RoupaCreateSerializer

        return RoupaSerializer
