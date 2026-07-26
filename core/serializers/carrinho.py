from rest_framework.serializers import ModelSerializer

from core.models import Carrinho


class CarrinhoSerializer(ModelSerializer):
    class Meta:
        model = Carrinho
        fields = ['id', 'usuario', 'roupa', 'quantidade']
        read_only_fields = ['id', 'usuario']
