
from django.db import models


class Carrinho(models.Model):
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='carrinhos')
    roupa = models.ForeignKey('Roupa', on_delete=models.CASCADE, related_name='carrinhos')
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.usuario} - {self.roupa} ({self.quantidade})'

    class Meta:
        verbose_name_plural = 'Carrinhos'
        constraints = [models.UniqueConstraint(fields=['usuario', 'roupa'], name='unique_roupa_usuario')]
