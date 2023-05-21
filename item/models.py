from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        ordering = ('nome',) #Aqui ordenamos as categorias em ordem alfabética.
        verbose_name_plural = 'Categorias' #Aqui eu altero a forma como o Django vai transformar em plural as palavras que eu escrever.

    def __str__(self):
        return self.nome #Aqui é para aparecerem os nomes das categorias, ao invés de 'categoria object'
    
    #Após criarmos as categorias, vamos criar os itens que irão se enquadrar em alguma categoria.

class Item(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='items', on_delete=models.CASCADE) #Esse Cascade, como visto na matéria Banco de Dados, quer dizer que se o conjunto Categoria for deletado, todos os itens atrelados a ele também serão deletados, por efeito cascata.
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    preco = models.FloatField()
    imagem = models.ImageField(upload_to='item_images', blank=True, null=True)
    vendido = models.BooleanField(default=False)
    vendedor = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)