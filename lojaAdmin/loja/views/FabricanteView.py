from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from ..forms.FabricanteForm import FabricanteForm
def list_fabricante_view(request, id=None):
    fabricante = request.GET.get("fabricante")
    fabricantes = Fabricante.objects.all()
    '''OBS: O nome dentro do parêntese indica como deve ser escrito o parâmetro na url do navegador para que a variável possa capturar o valor do navegador'''
    if fabricante is not None: fabricantes = fabricantes.filter(Fabricante__contains=fabricante)
    if id is not None: fabricantes = fabricantes.filter(id=id)
    print(fabricantes)
    # Adicione para definir o contexto e carregar o template
    context = {
        'fabricantes': fabricantes
    }
    return render(request, template_name='fabricante/fabricante.html', context=context, status=200)

def edit_fabricante_view(request, id):
    fabricante = Fabricante.objects.get(pk=id)
    message = None
    if request.method == 'POST':
        fabricanteForm = FabricanteForm(request.POST, instance=fabricante, current_user=request.user)
    else:
        fabricanteForm = FabricanteForm(instance=fabricante, current_user=request.user)
    if fabricanteForm.is_valid():
        fabricanteForm.save()
        message = { 'type': 'success', 'text': 'Fabricante atualizado com sucesso' }
    else:
        message = { 'type': 'warning', 'text': 'Erro detectado' }
    context = {
        'fabricanteForm': fabricanteForm,
        'message': message
    }
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)