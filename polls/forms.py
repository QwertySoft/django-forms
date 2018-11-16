# Importamos los módulos que necesitasmos
from django.forms import ModelForm, Select
from polls.models import Question
from django.utils.translation import gettext_lazy as _

# Definimos un formulario para el modelo Question
class QuestionForm(ModelForm):
    class Meta:
        model = Question
        # Declaramos los campos que queremos renderizar
        fields = ('name', 'target', 'reporter')
        # Definimos los labels a mostrar junto con los inputs
        labels = {
            'name': _('Nombre completo'),
            'target': _('Público objetivo'),
            'reporter': _('Reportero')
        }