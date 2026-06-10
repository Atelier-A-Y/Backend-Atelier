
from django.db import models


class Compra(models.Model):
    endereco = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return f'Compra - {self.id} '
