from django.shortcuts import render, redirect, reverse
from .models import Prato, Funcionario, Cliente, Pedido
from .forms import PratoForm, CadastroForm, PedidoForm
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.generic.edit import FormView


def lista_pratos(request):
    if request.user.is_authenticated:
        lista = Prato.objects.all()
        if Funcionario.objects.filter(usuario = request.user):
            return render(request, 'app_delivery/lista_funcionario.html', {'lista_pratos': lista})
        elif Cliente.objects.filter(usuario = request.user):
            return render(request, 'app_delivery/lista_cliente.html', {'lista_pratos': lista})
    else:
        return render(request, 'app_delivery/login.html', {})

def lista_pedidos(request):
    if request.user.is_authenticated:
        listaP = Pedido.objects.filter(atendido=False)
        if Funcionario.objects.filter(usuario = request.user):
            return render(request, 'app_delivery/lista_pedidos.html', {'lista_pedidos': listaP})
        
    else:
        return render(request, 'app_delivery/login.html', {})


def meusPedidos(request):
    if request.user.is_authenticated:
        listaP = Pedido.objects.filter(cliente__usuario = request.user)
        return render(request, 'app_delivery/meus_pedidos.html', {'meu_pedido': listaP})
    else:
        return render(request, 'app_delivery/login.html', {})


def cadastrar_prato(request):
    if request.method == 'GET':
        if request.user:
            form = PratoForm()
            return render(request, 'app_delivery/cadastrar_prato.html', {'form': form})
        else:
            redirect('/autenticacao/login')
    elif request.method == 'POST':
        prato = Prato()
        prato.nome = request.POST.get('nome')
        prato.descricao = request.POST.get('descricao')
        prato.valor = request.POST.get('valor')
        prato.save()

        return redirect(reverse('lista_pratos'))

def delete_prato(request, id):
    if request.user.is_authenticated:
        funcionario = Funcionario.objects.get(usuario = request.user)
        if funcionario.cargo == 'Funcionário':
            prato = Prato.objects.get(pk=id)
            prato.delete()
            return redirect(reverse('lista_pratos'))
        else:
            return render(request, 'app_delivery/erro.html', {'mensagem_erro': 'Você tentou acessar um recurso que não esta disponivel.'})
    else:
        redirect('/autenticacao/login')

class CadastroView(FormView):
    template_name = 'app_delivery/cadastrar_cliente.html'
    form_class = CadastroForm
    def form_valid(self, form):
        dados = form.clean()
        senha = make_password(dados['senha'])
        usuario = User(username=dados['usuario'], password=senha)
        cliente = Cliente(usuario = usuario, nome=dados['nome'], cpf=dados['cpf'],
                        cep=dados['cep'], logradouro=dados['logradouro'],
                        complemento=dados['complemento'])
        usuario.save()
        cliente.save()

        return super().form_valid(form)
    def get_success_url(self):
        return reverse('login')

def aceitar_pedido(request, id):
    if request.user.is_authenticated:
        funcionario = Funcionario.objects.get(usuario = request.user)
        if funcionario.cargo == 'Funcionário':
            pedido = Pedido.objects.get(pk=id)
            pedido.aceitar = True
            pedido.status = 2
            pedido.save()
            return redirect(reverse('lista_pedidos'))
        else:
            return render(request, 'app_delivery/erro.html', {'mensagem_erro': 'Você tentou acessar um recurso que não esta disponivel.'})
    else:
        redirect('/autenticacao/login')

def pronto_pedido(request, id):
    if request.user.is_authenticated:
        funcionario = Funcionario.objects.get(usuario = request.user)
        if funcionario.cargo == 'Funcionário':
            pedido = Pedido.objects.get(pk=id)
            pedido.pronto = True
            pedido.status = 3
            pedido.save()
            return redirect(reverse('lista_pedidos'))
        else:
            return render(request, 'app_delivery/erro.html', {'mensagem_erro': 'Você tentou acessar um recurso que não esta disponivel.'})
    else:
        redirect('/autenticacao/login')

def atendimento(request, id):
    if request.user.is_authenticated:
        funcionario = Funcionario.objects.get(usuario = request.user)
        if funcionario.cargo == 'Funcionário':
            pedido = Pedido.objects.get(pk=id)
            pedido.atendido = True
            pedido.save()
            return redirect(reverse('lista_pedidos'))
        else:
            return render(request, 'app_delivery/erro.html', {'mensagem_erro': 'Você tentou acessar um recurso que não esta disponivel.'})
    else:
        redirect('/autenticacao/login')


def Pedido_Realizar(request):
    if request.method == 'GET':
        if request.user:
            form = PedidoForm()
            return render(request, 'app_delivery/fazer_pedido.html', {'form': form})
        else:
            redirect('/autenticacao/login')
    elif request.method == 'POST':
        ped = Pedido()
        cliente = Cliente.objects.get(usuario = request.user)
        ped.cliente = cliente
        pratos = request.POST['pedido'] 
        ped.status = 1
        ped.save()
        ped.prato.add(pratos)
        
        return redirect(reverse('meu_pedido'))
        
