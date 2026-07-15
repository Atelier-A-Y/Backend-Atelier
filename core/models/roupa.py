from django.conf import settings
from django.db import models

from uploader.models import Image


class Roupa(models.Model):
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=50, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    foto = models.ForeignKey(
        Image,
        related_name='+',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome


class Carrinho(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )


class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(
        Carrinho,
        on_delete=models.CASCADE,
        related_name="itens"
    )

    roupa = models.ForeignKey(
        Roupa,
        on_delete=models.CASCADE
    )

    quantidade = models.PositiveIntegerField(default=1)
