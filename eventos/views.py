from django.shortcuts import render

# from django.shortcuts import redirect

# from .forms import EventoModelForm

# from .forms import ContatoForm, EventoModelForm

from .models import Evento
from django.core.paginator import Paginator

"""
def evento(request):
    context = {
        'eventos': Evento.objects.all().order_by('data_publicacao')
    }

    return render(request, 'eventos/index.html', context)
"""


def evento(request):
    eventos = Evento.objects.all().order_by("data_publicacao")
    paginator = Paginator(eventos, 5)

    page = request.GET.get('p')
    eventos = paginator.get_page(page)

    return render(request, 'eventos/index.html', {'eventos': eventos})
