# Generated by Django 3.1.4 on 2021-01-10 21:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_comentario', models.CharField(max_length=150, verbose_name='Nome')),
                ('email_comentario', models.EmailField(max_length=254, verbose_name='Email')),
                ('comentario', models.TextField(verbose_name='Comentário')),
                ('data_comentario', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data')),
                ('publicado_comentario', models.BooleanField(default=False, verbose_name='Publicado')),
                ('post_comentario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.post', verbose_name='Post')),
                ('usuario_comentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]