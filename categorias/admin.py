from django.contrib import admin
from . models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    list_diplay = ('id', 'nome_cat')
    list_diplay_links = ('id', 'nome_cat')


admin.site.register(Categoria, CategoriaAdmin)
