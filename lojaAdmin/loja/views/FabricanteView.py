from django.shortcuts import render, redirect, get_object_or_404
from loja.models import Fabricante
from loja.forms.ObjFabricanteForm import ObjFabricanteForm, ObjForm

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

def edit_fabricante_view(request):
    usuario = Usuario.objects.filter(user=request.user).first()
    emailUnused = True
    message = None
    if request.method == 'POST':
        usuarioForm = UserUsuarioForm(request.POST, instance=usuario, current_user=request.user)
        userForm = UserForm(request.POST, instance=request.user)
        # Verifica se o e-mail que o usuário está tentando utilizar
        # em seu perfil já existe em outro perfil
        verifyEmail = Usuario.objects.filter(user__email=request.POST['email']).exclude(user__id=request.user.id).first()
        emailUnused = verifyEmail is None
    else:
        usuarioForm = ObjFabricanteForm(instance=fabricante, current_user=request.user)
        objForm = ObjForm(instance=request.user)
    if usuarioForm.is_valid() and objForm.is_valid():
        usuarioForm.save()
        objForm.save()
        message = { 'type': 'success', 'text': 'Fabricante atualizado com sucesso' }
    else:
        message = { 'type': 'warning', 'text': 'Erro detectado' }
        #     # Aqui verificamos se é do tipo post, para que na primeira vez que a página
        #     #carregar a mensagem não apareça, já que no primeiro carregamento não enviamos um post, o
        #     #form é dado como inválido e entra aqui.
        #     if request.method == 'POST':
        #         if emailUnused:
        #             # Se o e-mail não está em uso tiver algum dado inválido.
        #             message = { 'type': 'danger', 'text': 'Dados inválidos' }
        #         else:
        #             # Se o e-mail já está em uso por outra pessoa.
        #             message = { 'type': 'warning', 'text': 'E-mail já usado' }
    context = {
        'fabricanteForm': fabricanteForm,
        'objForm': objForm,
        'message': message
    }
    return render(request, template_name='fabricante/fabricante-edit.html', context=context, status=200)