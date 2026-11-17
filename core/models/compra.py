from django.db import models


class Compra(models.Model):
    endereco = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey(
        'core.User', 
        on_delete=models.CASCADE, 
        related_name='compras', 
        blank=True, 
        null=True
    )

    produtos = models.ManyToManyField(
        'core.roupa',
        related_name='compras_envolvidas',
        blank=True
    )

    status = models.CharField(max_length=50, default='Pedido a caminho')

    def __str__(self):
        return f'Compra - {self.id}'

    @property
    def preco_total(self):
        return sum(produto.preco for produto in self.produtos.all() if produto.preco)
