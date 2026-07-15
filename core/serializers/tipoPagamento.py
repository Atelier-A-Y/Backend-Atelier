from rest_framework.serializers import ModelSerializer

from core.models import TipoPagamento


class TipoPagamentoSerializer(ModelSerializer):
    class Meta:
        model = TipoPagamento
        fields = '__all__'
