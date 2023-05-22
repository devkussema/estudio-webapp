from django.shortcuts import render
from django.urls import resolve

# Create your views here.
def index(request):
    resolver_match = resolve(request.path)
    rota_nomeada_atual = resolver_match.url_name
    contexto = {
        'rota_atual': rota_nomeada_atual
    }
    return render(request, 'paginas/index.html', contexto)

def sobre(request):
    return render(request, 'paginas/sobre.html')

def portfolio(request):
    return render(request, 'paginas/portfolio.html')

def blog(request):
    return render(request, 'paginas/blog.html')

def contato(request):
    return render(request, 'paginas/contato.html')
