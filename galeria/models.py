from django.db import models

from django.utils import timezone

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True),
    modificado = models.DateField('Data de Atualização', auto_now=True),
    ativo = models.BooleanField('Ativo?', default=True),
    titulo = models.CharField(max_length=200)

    data_criacao = models.DateTimeField(default=timezone.now)
    data_publicacao = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.titulo

    class Meta:
        abstract = True


class Foto(Base):
    titulo = models.CharField('Título', max_length=100)
    autor = models.CharField('Autor', max_length=100)
    lugar = models.CharField('local', max_length=50)
    imagem = models.ImageField(upload_to='foto/%Y/%m/%d')
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def publicar(self):
        self.criado = timezone.now()
        self.save()

    def __std__(self):
        return self.titulo


def foto_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.titulo)


signals.pre_save.connect(foto_pre_save, sender=Foto)
