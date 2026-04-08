from django.db import models


class Venda(models.Model):
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venda {self.id}'
