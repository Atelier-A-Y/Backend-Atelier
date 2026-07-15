from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Roupa, Carrinho, ItemCarrinho
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

        carrinho, _ = Carrinho.objects.get_or_create(
            usuario=request.user
        )

        roupa = self.get_object()

        item, criado = ItemCarrinho.objects.get_or_create(
            carrinho=carrinho,
            roupa=roupa,
        )

        if not criado:
            item.quantidade += request.data.get("quantidade", 1)

        item.save()

        return Response({"mensagem": "Produto adicionado"})
