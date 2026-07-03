from django.db import models

from .categoria import Categoria
from .continente import Continente


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    continente = models.ForeignKey(Continente, on_delete=models.SET_NULL, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    tamanho = models.ForeignKey('Tamanho', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nome
