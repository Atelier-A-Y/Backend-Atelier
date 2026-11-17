from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Compra
from core.serializers.roupa import RoupaRetrieveSerializer


class CompraSerializer(ModelSerializer):
    produtos = RoupaRetrieveSerializer(many=True, read_only=True)
    preco_total = SerializerMethodField()

    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ('user',)

    def get_preco_total(self, obj):
        # Soma o preço de todas as roupas vinculadas a esta compra
        return sum(produto.preco for produto in obj.produtos.all() if produto.preco)
