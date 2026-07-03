from rest_framework import viewsets

from core.models import CompraFornecedor, Fornecedor
from core.serializers import CompraFornecedorSerializer, FornecedorSerializer


class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer


class CompraFornecedorViewSet(viewsets.ModelViewSet):
    queryset = CompraFornecedor.objects.all()
    serializer_class = CompraFornecedorSerializer
