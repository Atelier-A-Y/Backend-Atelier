from rest_framework.viewsets import ModelViewSet

from core.models import TipoPagamento
from core.serializers import TipoPagamentoSerializer


class TipoPagamentoViewSet(ModelViewSet):
    queryset = TipoPagamento.objects.all()
    serializer_class = TipoPagamentoSerializer
