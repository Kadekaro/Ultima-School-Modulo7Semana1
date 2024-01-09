from django.db import models


# Create your models here.
class Contato(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)


class Reserva(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=75)
    mensagem = models.TextField(blank=True)
    data = models.DateTimeField()
