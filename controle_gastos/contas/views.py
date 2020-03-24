from django.shortcuts import render, redirect # Importa o redirect
from .models import Transacao  # Importa o model
from .form import TransacaoForm  # Importa a classe do form


def deletar_transacao(request, pk):  # Cria a função de delete,
    # que recebe a pk, para saber qual registro deletar
    transacao = Transacao.objects.get(pk=pk)  # Cria a variave transacao que
    # recebe do banco a transação referente a PK que a view recebeu
    transacao.delete()  # Deleta a transação
    return redirect('url_listagem')  # Redireciona para listagem


def atualizar_transacao(request, pk):  # Cria a função de update,
    # que recebe a pk, para saber qual registro atualizar
    data = {}  # Cria um dicionário vazio
    transacao = Transacao.objects.get(pk=pk)  # Cria a variave transacao que
    # recebe do banco a transação referente a PK que a view recebeu
    form = TransacaoForm(request.POST or None, instance=transacao)  # Cria
    # um form recebendo os dados da transacao referente à PK
    if form.is_valid():  # Testa se o form é valido
        form.save()  # Salva os dados no Banco de Dados
        return redirect('url_listagem')  # Redireciona
    data['form'] = form  # Adiciona o form criado no dicionario
    return render(request, "contas/cadastro.html", data)


def cadastro_transacao(request):  # Cria a função de cadastro
    data = {}  # Cria um dicionário vazio
    form = TransacaoForm(request.POST or None)  # Cria um form
    # recebendo os dados do POST do bt Salvar ou vazio
    if form.is_valid():  # Testa se o form é valido
        form.save()  # Salva os dados no Banco de Dados
        return redirect('url_listagem')  # Redireciona
    data['form'] = form  # Adiciona o form criado no dicionario
    return render(request, "contas/cadastro.html", data)


def listagem(request):
    data = {}  # Cria um dicionário vazio
    data["transacoes"] = Transacao.objects.all()  # objects é um manager pronto
    # do Django que nos permitirá acessar os dados de determinado model
    return render(request, "contas/listagem.html", data)


def home(request):
    return render(request, "contas/home.html")
'''Retorna um render permitindo renderizar um template , passando
como parametrosa request e o nome e caminho do template '''
