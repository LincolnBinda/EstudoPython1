from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    minha_variavel = 'Programe Facil'
    sexo = 'm'
    nome = 'Pedro'

    lista = [
        {'nome': 'Lucas', 'sexo': 'm'},
        {'nome': 'Maria', 'sexo': 'f'},
        {'nome': 'Joaquina', 'sexo': 'f'},
        {'nome': 'Pedro', 'sexo': 'm'}
    ]

    data = {'minha_variavel': minha_variavel, 'sexo': sexo, 'nome': nome, 'lista': lista}
    return render(request, 'index.html', data)