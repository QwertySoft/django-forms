# Importamos los mósulos necesarios
from django.urls import path
from . import views

# URLConf que define las URLs para nuestra app 'polls'
urlpatterns = [
    path('', views.index, name='polls_index'),
    path('new', views.add, name='polls_add'),
    path('<int:poll_id>', views.detail, name='poll_detail'),
]
