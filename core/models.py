from django.db import models
from django.contrib.auth.models import User

class Publicacao(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    gostos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.autor.username} - {self.conteudo[:20]}"