from django.http import HttpResponse
def list_produto_view(request, id=None):
    if id is 74:
        return HttpResponse('<h1>Easter Egg!!</h1>')
    return HttpResponse('<h1>Produto de id %s!</h1>' % id)

'''se quiser definir um id padrão para ou uma mensagem padrão para quando o valor for
recebido basta ir no medoto list_produto_view do ProdutoView.py e antes do return
colocar:
if id is None:
id = 0
Ou
if id is None:
return HttpResponse('<h1>Nenhum id foi informado</h1>')'''