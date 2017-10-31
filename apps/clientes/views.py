from django.shortcuts import render
from apps.clientes.models import Cliente


def listaClientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'listaClientes': clientes})


def nuevoCliente(request):
    pass


def verCliente(request):
    pass


def editarCliente(request):
    pass


def eliminarCliente(request):
    pass






