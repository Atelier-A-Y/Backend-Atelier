from django.db import models


class Carrinho(models.Model):
    quantidade = models.PositiveIntegerField(default=0)
    roupa = models.ForeignKey('Roupa', on_delete=models.CASCADE, related_name='carrinhos')
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='carrinhos')

    def __str__(self):
        return str(self.quantidade)

    class Meta:
        verbose_name_plural = 'Carrinhos'
