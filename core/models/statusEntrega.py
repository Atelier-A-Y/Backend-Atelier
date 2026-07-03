from django.db import models


class StatusEntrega(models.Model):
    status = models.CharField(max_length=100, blank=True, null=True)
    localizacao = models.CharField(max_length=100, blank=True, null=True)
    data_atualizada = models.DateTimeField(auto_now=True, blank=True, null=True)
    compra = models.ForeignKey('core.Compra', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = 'Status de Entrega'
