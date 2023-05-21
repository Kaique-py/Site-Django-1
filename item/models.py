from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categorias' #Aqui eu altero a forma como o Django vai transformar em plural as palavras que eu escrever.