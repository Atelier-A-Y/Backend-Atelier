from django.db import models


class TipoPagamento(models.Model):
    nome_tipoPagamento = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.nome_tipoPagamento
