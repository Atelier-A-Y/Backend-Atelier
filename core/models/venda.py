from django.db import models

from .tipoPagamento import TipoPagamento


class Venda(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.PROTECT, related_name='vendas', null=True, blank=True)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_venda = models.DateTimeField(auto_now_add=True)
    tipo_pagamento = models.ForeignKey(TipoPagamento, on_delete=models.SET_NULL, null=True, blank=True, related_name='vendas')

    def __str__(self):
        return f'Venda #{self.id}'


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE, related_name='itens')
    roupa = models.ForeignKey('Roupa', on_delete=models.PROTECT, related_name='itens_venda')
    quantidade = models.PositiveIntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantidade}x {self.roupa.nome}'