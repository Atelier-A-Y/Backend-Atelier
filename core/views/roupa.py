from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from core.models import Carrinho, Roupa
from core.serializers.roupa import (
    RoupaCreateSerializer,
    RoupaRetrieveSerializer,
    RoupaSerializer,
)


class RoupaViewSet(ModelViewSet):
    queryset = Roupa.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['categoria__descricao', 'editora__nome']
    search_fields = ['titulo']
    ordering_fields = ['titulo', 'preco']
    ordering = ['titulo']

    def get_serializer_class(self):
        if self.action in {'retrieve', 'list'}:
            return RoupaRetrieveSerializer

        if self.action in {'create', 'update', 'partial_update'}:
            return RoupaCreateSerializer

        return RoupaSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def adicionar_carrinho(self, request, pk=None):
        roupa = self.get_object()

        quantidade = int(request.data.get('quantidade', 1))

        carrinho, criado = Carrinho.objects.get_or_create(
            usuario=request.user, roupa=roupa, defaults={'quantidade': quantidade}
        )

        if not criado:
            carrinho.quantidade += quantidade
            carrinho.save()

        return Response({'mensagem': 'Produto adicionado ao carrinho', 'quantidade': carrinho.quantidade})
