from django.urls import path
# from .views import index, contato, foto
from .views import index, foto

urlpatterns = [

    path('', index, name='index.html'),
    path('foto/', foto, name='foto'),
    # path('contato/', contato, name='contato'),
    # path('', index, name='index'),

    # path('foto/', foto, name='foto'),
]
