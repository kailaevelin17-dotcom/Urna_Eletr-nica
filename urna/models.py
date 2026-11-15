from django.db import models


class Candidato(models.Model):

    numero = models.IntegerField(unique=True)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(
        upload_to='candidatos/',
        null=True,
        blank=True
    )
    partido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.numero} — {self.nome}"


class Votacao(models.Model):

    votos_brancos = models.IntegerField(default=0)

    def __str__(self):
        return "Votação"