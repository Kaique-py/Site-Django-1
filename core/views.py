from django.shortcuts import render

# Create your views here.
#Aqui no arquivo views vamos criar todas as páginas que forem existir no meu site.

#Iniciamos criando uma página chamada index, que será nossa front page.
def index(request):
    return render(request, 'core/index.html')

#Na sequência vamos criando as páginas a seguir:
def contact(request):
    return render(request, 'core/contact.html')