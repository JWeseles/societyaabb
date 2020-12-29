from django.contrib import admin

from .models import Foto


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'lugar', 'imagem', 'slug', 'ativo')
    list_per_page = 10

