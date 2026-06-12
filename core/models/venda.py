from django.db import models

from .tipoPagamento import TipoPagamento


class Venda(models.Model):
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    tipoPagamento = models.ForeignKey(TipoPagamento, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'Venda {self.id}'
