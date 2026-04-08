
from django.db import models


class Compras(models.Model):

    nome = models.CharField(max_length=255)
    endereco = models.CharField(max_length=32, null=True, blank=True)
    tipo_pagamento = models.IntegerField(default=0, null=True, blank=True)
    preco = models.DecimalField(max_digits=7, decimal_places=2, default=0)

    def __str__(self):
        return f'({self.id}) {self.nome} ({self.tipo_pagamento})'
