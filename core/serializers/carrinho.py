from rest_framework import serializers

from core.models import Carrinho, Roupa
from core.serializers.roupa import RoupaRetrieveSerializer


class CarrinhoSerializer(serializers.ModelSerializer):
    roupa_detalhes = RoupaRetrieveSerializer(
        source='roupa',
        read_only=True
    )

    roupa = serializers.PrimaryKeyRelatedField(
        queryset=Roupa.objects.all()
    )

    usuario = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Carrinho
        fields = [
            'id',
            'usuario',
            'roupa',
            'roupa_detalhes',
            'quantidade',
        ]