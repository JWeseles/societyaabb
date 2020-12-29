from django.urls import path

# from .views import index, contato, evento
# from polls.views import EventosView
from .views import evento

urlpatterns = [
    # path('', index, name='index'),
    path('', evento, name='index.html'),
    # path('contato/', contato, name='contato'),
    # path('eventos/', evento, name='eventos'),
    # path('', EventosView.as_view(), name='index.html'),
]
