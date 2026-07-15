from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CarrinhoViewSet(ViewSet):
    permission_classes = [IsAuthenticated]

    def list(self, request):

        carrinho, _ = Carrinho.objects.get_or_create(usuario=request.user)

        itens = ItemCarrinho.objects.filter(carrinho=carrinho)

        serializer = ItemCarrinhoSerializer(itens, many=True)

        return Response(serializer.data)
