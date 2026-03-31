from django.db import models


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
