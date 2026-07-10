from django.shortcuts import render, redirect
from loja.models import Categoria
from django.utils import timezone

def list_categoria_view(request, id=None):

    categoria = request.GET.get("categoria")
    categorias = Categoria.objects.all()
    '''OBS: O nome dentro do parêntese indica como deve ser escrito o parâmetro na url do navegador para que a variável possa capturar o valor do navegador'''
    if categoria is not None: categorias = categorias.filter(Categoria__contains=categoria)
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
    print("postback-details")
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-details.html', context=context, status=200)

def delete_categoria_view(request, id=None):
    # Processa o evento GET gerado pela action
    categorias = Categoria.objects.all()
    if id is not None:
        categorias = categorias.filter(id=id)
    categoria = categorias.first()
    print("postback-delete")
    print(categoria)
    context = {'categoria': categoria}
    return render(request, template_name='categoria/categoria-delete.html', context=context,status=200)


def delete_categoria_postback(request, id=None):
    if request.method == 'POST':
        id = request.POST.get("id")
        try:
            categoria_obj = Categoria.objects.get(id=id)
            categoria_obj.delete()
            print("Categoria excluida com sucesso")
            
        except Categoria.DoesNotExist:
            print("Erro: Categoria com o ID %s não foi encontrado." % id)
        except Exception as e:
            print("Erro excluindo a categoria: %s" % e)
            
    return redirect("/categoria")


def create_categoria_view(request, id=None):

    if request.method == 'POST':
        categoria = request.POST.get("Categoria")
        print("postback-create")
        print(categoria)
        try:
            obj_categoria = Categoria()
            obj_categoria.Categoria = categoria
            obj_categoria.criado_em = timezone.now()
            obj_categoria.alterado_em = obj_categoria.criado_em
            obj_categoria.save()
            print("Categoria %s salva com sucesso" % categoria)
            
        except Exception as e:
            print("Erro inserindo categoria: %s" % e)
        return redirect("/categoria")
    return render(request, template_name='categoria/categoria-create.html',status=200)

