from rest_framework.serializers import ModelSerializer

from core.models import Venda


class VendaSerializer(ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'preco_total']
