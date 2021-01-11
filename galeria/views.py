from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# from .forms import ContatoForm, FotoModelForm
from .forms import FotoModelForm
from .models import Foto
from django.core.paginator import Paginator

"""
def index(request):
    context = {
        'imagens': Foto.objects.all().order_by("autor")
    }
    
    return render(request, 'galeria/index.html', context)
"""


def index(request):
    imagens = Foto.objects.all().order_by("autor")
    paginator = Paginator(imagens, 5)

    page = request.GET.get('p')
    imagens = paginator.get_page(page)

    return render(request, 'galeria/index.html', {'imagens': imagens})


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
    return render(request, 'galeria/contato.html', context)
"""


def foto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = FotoModelForm(request.POST, request.FILES)
            if form.is_valid:

                form.save()

                messages.success(request, 'Imagem salva com sucesso.')
                form = FotoModelForm()
            else:
                messages.error(request, 'Erro ao salvar imagem')
        else:
            form = FotoModelForm()
        context = {
            'form': form
        }

        return render(request, 'galeria/foto.html', context)
    else:
        return redirect('index.html')
