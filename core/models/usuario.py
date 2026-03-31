from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.URLField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome
