from django.contrib import admin
from .models import Postagem


@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'data_criacao', 'data_publicacao')
    list_display_links = ('titulo', 'autor', 'data_criacao', 'data_publicacao')

    list_per_page = 3
