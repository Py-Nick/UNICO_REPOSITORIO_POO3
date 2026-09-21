from django.shortcuts import render, get_object_or_404, redirect
from loja.models import Produto, Favorito, FavoritoItem, Usuario
# from datetime import datetime
from django.contrib.auth.decorators import login_required
# from django.utils import timezone

def remover_favoritaritem_view(request, item_id):
    item = get_object_or_404(FavoritoItem, id=item_id)
    # Verifica se o item pertence ao favorito do usuário (opcional)
    favorito_id = request.session.get('favorito_id')
    if favorito_id == item.favorito.id:
        item.delete()
    return redirect('list_favorito')
    
def list_favoritaritem_view(request):

    print ('list_favorito_view')
    favorito = None
    favorito_item = None
    
    # Tenta pegar o favorito da sessão ou cria um novo favorito
    favorito_id = request.session.get('favorito_id')
    if favorito_id:
        print ('favorito: ' + str(favorito_id))
        # Obtém o favorito do usuário
        favorito = Favorito.objects.filter(id=favorito_id).first()
        if favorito:
            # Verifica se o produto já existe no favorito do usuário
            favorito_item = FavoritoItem.objects.filter(favorito_id=favorito_id)
            print ('itens favoritados encontrado: ' + str(favorito_item))
    context = {
        'favorito': favorito,
        'itens': favorito_item
    }
    return render(request, 'favorito/favorito-listar.html', context=context)
    
# Função para adicionar um item ao favoritos
def create_favoritaritem_view(request, produto_id=None):

    print ('create_favoritaritem_view')
    produto = get_object_or_404(Produto, pk=produto_id)

    if produto:
        print('produto: ' + str(produto.id))
     # Tenta pegar o favorito da sessão ou cria um novo favorito
    favorito_id = request.session.get('favorito_id')
    print ('favorito: ' + str(favorito_id))
    favorito = None

    if favorito_id:
        # Se o favorito já estiver na sessão, tentamos obter o favorito
        favorito = Favorito.objects.filter(id=favorito_id).first()
        print (favorito)
        print ('favorito1: ' + str(favorito.id))

    else:
        # Se o favorito não existir na sessão, cria um novo favorito
        favorito = Favorito.objects.create()
        # Armazena o ID do favorito na sessão
        request.session['favorito_id'] = favorito.id
        print ('favorito2: ' + str(favorito.id))
        # Verifica se o produto já existe no favoritos do usuário
    favorito_item = FavoritoItem.objects.filter(favorito=favorito, produto=produto).first()

    if favorito_item:
        # Se o produto já estiver no favoritos, apenas aumenta a quantidade
        favorito_item.quantidade += 1
        print ('item de favorito: Acrescentou 1 item do produto ' + str(favorito_item.id))

    else:
        # Se o produto não estiver no favorito, cria um novo item no favorito
        favorito_item = FavoritoItem.objects.create(
            favorito=favorito,
            produto=produto,
            quantidade=1,
            preco=produto.preco
        )
        print ('item de favorito: Acrescentou o produto ' + str(favorito_item.id))
    
    favorito_item.save()
    print ('item de favorito salvo: ' + str(favorito_item.id))
    return redirect('list_favorito')