from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Carrinho, Roupa
from core.serializers.roupa import (
    RoupaCreateSerializer,
    RoupaRetrieveSerializer,
    RoupaSerializer,
)


class RoupaViewSet(ModelViewSet):
    queryset = Roupa.objects.all()

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return RoupaRetrieveSerializer

        if self.action in ['create', 'update', 'partial_update']:
            return RoupaCreateSerializer

        return RoupaSerializer

@action(detail=True, methods=["post"], permission_classes=[IsAuthenticated])
def adicionar_carrinho(self, request, pk=None):

    roupa = self.get_object()

    carrinho, _ = Carrinho.objects.get_or_create(
        usuario=request.user
    )

    carrinho.roupa = roupa
    carrinho.save()

    return Response({"mensagem": "Produto adicionado"})
