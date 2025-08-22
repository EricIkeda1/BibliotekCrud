from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    genero = models.CharField(max_length=100, blank=True)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField(default=timezone.now)
    data_devolucao = models.DateTimeField(default=timezone.now() + timedelta(days=7))
    devolvido = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.usuario.username} -> {self.livro.titulo}"
