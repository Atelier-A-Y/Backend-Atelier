from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from core.models import Compra, Roupa
from core.serializers.roupa import RoupaRetrieveSerializer


class CompraSerializer(ModelSerializer):
    produtos = RoupaRetrieveSerializer(many=True, read_only=True)

    produtos_ids = serializers.PrimaryKeyRelatedField(
        many=True, 
        queryset=Roupa.objects.all(), 
        write_only=True,
        source='produtos'
    )

    preco_total = SerializerMethodField()

    class Meta:
        model = Compra
        fields = '__all__'
        read_only_fields = ('user',)

    def get_preco_total(self, obj):
        return sum(produto.preco for produto in obj.produtos.all() if produto.preco)
