# Importamos los módulos necesarios
from django.shortcuts import render
from django.http import HttpResponse
from polls.forms import QuestionForm
from polls.models import Question

# Definimos una vista mostrar el index
def index(request):
    # Renderizamos el HTML index.html y lo devolvemos al cliente
    return render(request, 'polls/index.html', {'name': 'UDE y Qwerty', 'poll_id': None, 'show_short': True, 'query_param': request.GET.get('query')})

# Definimos una vista mostrar el detalle
def detail(request, poll_id=None):
    # Renderizamos el HTML index.html con datos de un detalle y lo devolvemos al cliente
    return render(request, 'polls/index.html', {'name': 'UDE y Qwerty', 'poll_id': poll_id, 'show_short': True, 'query_param': request.GET.get('query')})

# Definimos una vista para agregar una pregunta
def add(request):
    # Implementamos el flujo GET
    if request.method == 'GET':
        # Creamos el formulario para preguntas
        form = QuestionForm()
        # Renderizamos el add.html con el formulario limpio
        return render(request, 'polls/add.html', {'form': form})
    # Implementamos el flujo POST
    elif request.method == 'POST':
        # Cargamos los datos posteados en un formulario
        form = QuestionForm(request.POST)
        # Guardamos los datos
        form.save()
        # Renderizamos el add.html con el formulario limpio y un mensaje de éxito
        return render(request, 'polls/add.html', {'form': QuestionForm(), 'message': 'Datos guardados correctamente'})