from django.db import models


class Continente(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.nome
    class Meta:
        verbose_name_plural = "Continentes"
