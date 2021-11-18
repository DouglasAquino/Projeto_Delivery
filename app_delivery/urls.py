from django.urls import path
from .views import lista_pratos, cadastrar_prato, delete_prato, CadastroView, lista_pedidos, aceitar_pedido
from .views import pronto_pedido, atendimento, Pedido_Realizar, meusPedidos
urlpatterns = [
    path('pratos', lista_pratos, name='lista_pratos'),
    path('pratos/pedidos', lista_pedidos, name='lista_pedidos'),
    path('pratos/cadastrar', cadastrar_prato, name='cadastrar_prato'),
    path('pratos/delete/<int:id>', delete_prato, name='delete_prato'),
    path('pratos/Cad_cliente', CadastroView.as_view() , name='cadastrar_cliente'),
    path('pratos/aceitar/<int:id>', aceitar_pedido, name='aceitar_pedido'),
    path('pratos/pronto/<int:id>', pronto_pedido, name='pronto_pedido'),
    path('pratos/atendimento/<int:id>', atendimento, name='atendimento_pedido'),
    path('pratos/pedido', Pedido_Realizar , name='fazer_pedido'),
    path('pratos/meus', meusPedidos , name='meu_pedido'),

    
]
