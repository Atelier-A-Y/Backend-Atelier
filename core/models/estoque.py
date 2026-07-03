from django.db import models


class Estoque(models.Model):
    roupa = models.OneToOneField('Roupa', on_delete=models.CASCADE, related_name='estoque')
    quantidade = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.roupa.nome} - {self.quantidade}'


class MovimentacaoEstoque(models.Model):

    class Tipo(models.TextChoices):
        ENTRADA = 'E', 'Entrada'
        SAIDA = 'S', 'Saída'

    roupa = models.ForeignKey('Roupa', on_delete=models.CASCADE, related_name='movimentacoes')
    tipo = models.CharField(max_length=1, choices=Tipo.choices)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    compra = models.ForeignKey('Compra', on_delete=models.SET_NULL, null=True, blank=True)
    venda = models.ForeignKey('Venda', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.roupa.nome} ({self.quantidade})'
