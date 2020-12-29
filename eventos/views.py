from django.shortcuts import render

# from django.shortcuts import redirect

# from .forms import EventoModelForm

# from .forms import ContatoForm, EventoModelForm

from .models import Evento


def evento(request):
    context = {
        'eventos': Evento.objects.all().order_by('data_publicacao')
    }

    return render(request, 'eventos/index.html', context)

"""
def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')
            form = ContatoForm()
    else:
        messages.error(request, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(request, 'contato.html', context)
"""

"""
def evento(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = EventoModelForm(request.POST, request.FILES)
            if form.is_valid:

                form.save()

                messages.success(request, 'Evento salvo com sucesso.')
                form = EventoModelForm()
            else:
                messages.error(request, 'Erro ao salvar evento')
        else:
            form = EventoModelForm()
        context = {
            'form': form
        }

        return render(request, 'eventos/index.html', context)
    else:
        return redirect('polls/index.html')
"""