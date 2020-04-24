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

