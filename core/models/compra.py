from django.db import models


class Compra(models.Model):
    endereco = models.CharField(max_length=32, null=True, blank=True)
    user = models.ForeignKey('core.User', on_delete=models.CASCADE, related_name='compras', blank=True, null=True)


def __str__(self):
    return f'Compra - {self.id} '
