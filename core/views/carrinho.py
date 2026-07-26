from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.models import Carrinho
from core.serializers import CarrinhoSerializer


class CarrinhoViewSet(ModelViewSet):
    serializer_class = CarrinhoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Carrinho.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        roupa = serializer.validated_data['roupa']
        quantidade = serializer.validated_data.get('quantidade', 1)

        carrinho, criado = Carrinho.objects.get_or_create(
            usuario=self.request.user,
            roupa=roupa,
            defaults={'quantidade': quantidade}
        )

        if not criado:
            carrinho.quantidade += quantidade
            carrinho.save()