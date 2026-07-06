#from django.http import HttpResponse
import os
from django.shortcuts import render, redirect
from loja.models import Categoria
from datetime import timedelta, datetime
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

def list_categoria_view(request, id=None):

    categoria = request.GET.get("categoria")
    categorias = Categoria.objects.all()
    '''OBS: O nome dentro do parêntese indica como deve ser escrito o parâmetro na url do navegador para que a variável possa capturar o valor do navegador'''

    #if categoria is not None: produtos = produtos.filter(categoria=categoria)
    #if fabricante is not None: produtos = produtos.filter(fabricante=fabricante)
    #produtos = Produto.objects.filter(Produto=produto) #procura o nome exato
    # produtos = Produto.objects.first()

    if categoria is not None: categorias = categorias.filter(categoria__Categoria=categoria)

    if id is not None: categorias = categorias.filter(id=id)
    print(categorias)
    # Adicione para definir o contexto e carregar o template
    context = {
    'categorias': categorias
    }
    return render(request, template_name='categoria/categoria.html', context=context, status=200)


def edit_categoria_view(request, id=None):
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = { 'categoria': categoria }
    return render(request, template_name='categoria/categoria-edit.html', context=context, status=200)

def edit_categoria_postback(request, id=None):
    if request.method == 'POST':
        # Salva dados editados
        id = request.POST.get("id")
        categoria = request.POST.get("Categoria")
        print("postback")
        print(id)
        print(categoria)
        try:
            obj_categoria = Categoria.objects.filter(id=id).first()
            obj_categoria.Categoria = categoria
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria)
        except Exception as e:
            print("Erro salvando edição de categoria: %s" % e)
    return redirect("/categoria")

def details_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-delete.html', context=context,status=200)


def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            categoria_obj = Categoria.objects.get(id=id)
            categoria_obj.delete()
            print("Produto excluido com sucesso")
            
        except Categoria.DoesNotExist:
            print("Erro: Categoria com o ID %s não foi encontrado." % id)
        except Exception as e:
            print("Erro excluindo a categoria: %s" % e)
            
    return redirect("/categoria")


def create_categoria_view(request, id=None):
    Categorias = Categoria.objects.all()
    context = {'categorias' : Categorias}

    # Processa o post back gerado pela action
    if request.method == 'POST':
        categoria = request.POST.get("categoria")
        print(categoria)
        try:
            obj_produto = Produto()
            obj_produto.Produto = produto
            obj_produto.save()
            print("Produto %s salvo com sucesso" % produto)
            
        except Exception as e:
            print("Erro inserindo produto: %s" % e)
        return redirect("/produto")
    return render(request, template_name='produto/produto-create.html', context=context ,status=200)

