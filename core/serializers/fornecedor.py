from rest_framework import serializers

from core.models import CompraFornecedor, Fornecedor, ItemCompraFornecedor


class FornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'


class ItemCompraFornecedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemCompraFornecedor
        fields = '__all__'


class CompraFornecedorSerializer(serializers.ModelSerializer):
    itens = ItemCompraFornecedorSerializer(many=True, read_only=True)

    class Meta:
        model = CompraFornecedor
        fields = '__all__'
