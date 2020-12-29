from django.contrib import admin

from .models import Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'lugar', 'slug', 'ativo')
    list_per_page = 10
