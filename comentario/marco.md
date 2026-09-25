# 3 bimestre - no processo para conclusão da atividade do capítulo 20 de POO3. Resta fazer a atividade: 3. Na interface de visualização de carrinho de compra confirmado mostrar os itens adquiridos do carrinho

# colocar javascript na página de carinho para fazer atualizações no banco para quando o usuário atualizar, atualizar o valor total 


```text
6. Uma observação sobre onde está sua view

Pelo seu import:

from loja.views.CarrinhoView import ...

sua estrutura parece ser algo como:

loja/
├── views/
│   ├── CarrinhoView.py
│   ├── ...
│
├── urls/
│   ├── CarrinhoUrls.py
│   ├── ...

Então a função:

def atualizar_quantidade(request, item_id):

precisa estar dentro de:

loja/views/CarrinhoView.py

E o import no CarrinhoUrls.py precisa incluí-la, como mostrei acima.

Portanto, neste momento, a estrutura fica:
config/urls.py
        │
        │  /carrinho/
        ▼
CarrinhoUrls.py
        │
        ├── "" ───────────────→ list_carrinho_view
        │
        ├── "<produto_id>" ───→ create_carrinhoitem_view
        │
        ├── "confirmar" ──────→ confirmar_carrinho_view
        │
        ├── "remover/<id>/" ──→ remover_item_view
        │
        └── "atualizar/<id>/" → atualizar_quantidade
                                  │
                                  ▼
                              CarrinhoItem
                                  │
                                  ▼
                            item.quantidade
                                  │
                                  ▼
                              item.save()

Uma correção importante antes de testar: sua atualizar_quantidade() precisa estar no CarrinhoView.py e o JsonResponse precisa estar importado lá:

from django.http import JsonResponse

Depois disso, podemos montar o carrinho-listar.html completo já integrado com seu CarrinhoUrls.py, em vez de você ter que juntar os pedaços manualmente.
```

usuario1 -> abacate123
usuario2 -> abacate123
admin -> admin