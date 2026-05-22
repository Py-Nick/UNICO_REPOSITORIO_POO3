#from django.http import HttpResponse
from django.shortcuts import render # Retire from django.http import HttpResponse
from loja.models import Produto
from datetime import timedelta, datetime
from django.utils import timezone

def list_produto_view(request, id=None):

    produto = request.GET.get("produto")
    destaque = request.GET.get("destaque")
    promocao = request.GET.get("promocao")
    categoria = request.GET.get("categoria")
    fabricante = request.GET.get("fabricante")
    dias = request.GET.get("dias")
    produtos = Produto.objects.all()
    '''OBS: O nome dentro do parêntese indica como deve ser escrito o parâmetro na url do navegador para que a variável possa capturar o valor do navegador'''
    
    produtos = Produto.objects.all() #instancia ojetos da classe produto, varre a tabela e monta uma lista
    if dias is not None:
        now = timezone.now()
        now = now - timedelta(days = int(dias))
        produtos = produtos.filter(criado_em__gte=now)
    
    if produto is not None: produtos = produtos.filter(Produto__contains=produto ) #desse jeito, a pesquisa é parcial. sai da igualdade e vai para o "oque contém X?"
    if promocao is not None: produtos = produtos.filter(promocao=promocao) #filtra o produto direto da tabela
    if destaque is not None: produtos = produtos.filter(destaque=destaque)

    #if categoria is not None: produtos = produtos.filter(categoria=categoria)
    #if fabricante is not None: produtos = produtos.filter(fabricante=fabricante)
    if categoria is not None: produtos = produtos.filter(categoria__Categoria=categoria)
    if fabricante is not None: produtos = produtos.filter(fabricante__Fabricante=fabricante) #desse jeito, a pesquisa é específica. não é pelo id.

    if id is not None: produtos = produtos.filter(id=id)
    print(produtos)
    # Adicione para definir o contexto e carregar o template
    context = {
    'produtos': produtos
    }
    return render(request, template_name='produto/produto.html', context=context, status=200)

    #produtos = Produto.objects.filter(Produto=produto) #procura o nome exato
    # produtos = Produto.objects.first()
    
    # if destaque is not None: print(destaque)
    # if produto is not None: print(produto)
    # if promocao is not None: print(promocao)
    # if categoria is not None: print(categoria)
    # if fabricante is not None: print(fabricante)
    if request is not None:
        return HttpResponse('<h1>Request identificado</h1>')
    elif id is None:
        return HttpResponse('<h1>Nenhum ID foi informado</h1>')
    elif id is 74:
        return HttpResponse('<h1>Easter Egg!!</h1>')
    return HttpResponse('<h1>Produto xx de id %s!</h1>' % id)

'''se quiser definir um id padrão para ou uma mensagem padrão para quando o valor for
recebido basta ir no medoto list_produto_view do ProdutoView.py e antes do return
colocar:
if id is None:
id = 0
Ou
if id is None:
return HttpResponse('<h1>Nenhum id foi informado</h1>')'''