from django.db import models


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome


class CompraFornecedor(models.Model):
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, related_name='compras')
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Compra {self.id} - {self.fornecedor.nome}'


class ItemCompraFornecedor(models.Model):
    compra = models.ForeignKey('CompraFornecedor', on_delete=models.CASCADE, related_name='itens')
    roupa = models.ForeignKey('Roupa', on_delete=models.CASCADE, related_name='itens_compra_fornecedor')
    quantidade = models.PositiveIntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.roupa.nome} - {self.quantidade} un.'

    @property
    def subtotal(self):
        return self.quantidade * self.preco
