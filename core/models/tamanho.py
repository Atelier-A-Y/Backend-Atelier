from django.db import models


class Tamanho(models.Model):
    nome = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Tamanhos'
