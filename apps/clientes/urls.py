from django.conf.urls import url
from apps.clientes import views

urlpatterns = [
    url(r'^lista_clientes/$', views.listaClientes, name='lista_clientes'),
    url(r'^crear_cliente/$', views.nuevoCliente, name='crear_cliente'),
    url(r'^ver_cliente/(?P<cliente_id>\d+)/$', views.verCliente, name='ver_cliente'),
    url(r'^editar_cliente/(?P<cliente_id>\d+)/$', views.editarCliente, name='editar_cliente'),
    url(r'^eliminar_cliente/(?P<cliente_id>\d+)/$', views.eliminarCliente, name='eliminar_cliente'),
]