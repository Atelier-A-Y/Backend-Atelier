from django.db import models

from .tipoPagamento import TipoPagamento


class Compra(models.Model):
    endereco = models.CharField(max_length=32, null=True, blank=True)
    tipoPagamento = models.ForeignKey(TipoPagamento, on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return f'Compra - {self.id} '
