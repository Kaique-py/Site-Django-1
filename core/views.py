from django.shortcuts import render

from item.models import Categoria, Item
# Create your views here.
#Aqui no arquivo views vamos criar todas as páginas que forem existir no meu site.

#Iniciamos criando uma página chamada index, que será nossa front page.
def index(request):
    itens = Item.objects.filter(vendido=False)[0:6]
    categorias = Categoria.objects.all()
    return render(request, 'core/index.html', {
        'categorias': categorias,
        'itens': itens,
    })

#Na sequência vamos criando as páginas a seguir:
def contact(request):
    return render(request, 'core/contact.html')