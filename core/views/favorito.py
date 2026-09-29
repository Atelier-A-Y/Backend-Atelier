from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Favorito
from core.serializers import FavoritoSerializer
from core.serializers.favorito import FavoritoRetrieveSerializer


class FavoritoViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Favorito.objects.filter(
            usuario=self.request.user
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return FavoritoRetrieveSerializer

        return FavoritoSerializer

    def perform_create(self, serializer):
        serializer.save(
            usuario=self.request.user
        )
