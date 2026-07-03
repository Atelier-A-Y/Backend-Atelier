from django.db import models


class Favorito(models.Model):
    roupa = models.ForeignKey('Roupa', on_delete=models.CASCADE, related_name='favoritos')
    usuario = models.ForeignKey('User', on_delete=models.CASCADE, related_name='favoritos')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Favorito: {self.roupa.id} - {self.usuario.id}'

    class Meta:
        verbose_name_plural = 'Favoritos'
