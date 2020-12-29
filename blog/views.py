from django.shortcuts import render
from blog.models import Postagem
from django.core.paginator import Paginator


def blog(request):
    postagens = Postagem.objects.all().order_by("-data_criacao")
    paginator = Paginator(postagens, 3)

    page = request.GET.get('p')
    postagens = paginator.get_page(page)

    return render(request, 'blog/blog.html', {'postagens': postagens})





