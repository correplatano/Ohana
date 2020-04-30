from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views.generic.base import View


def first_view(request):
    context = {
        'logo': 'Ohana Global Solutions'
    }
    return render(request, 'index.html', context)


class SobreNosotrosView(View):
    def get(self, request):
        return render(request, 'sobrenosotros.html')


class CafeView(View):
    def get(self, request):
        return render(request, 'cafe.html')


class BebidasCalientesView(View):
    def get(self, request):
        return render(request, 'bebidas-calientes.html')


class BebidasFriasView(View):
    def get(self, request):
        return render(request, 'bebidas-frias.html')


class SnacksView(View):
    def get(self, request):
        return render(request, 'snacks.html')


class ServiciosView(View):
    def get(self, request):
        return render(request, 'servicios.html')


class PromocionesView(View):
    def get(self, request):
        return render(request, 'promociones.html')


class ContactoView(View):
    def get(self, request):
        return render(request, 'contacto.html')

