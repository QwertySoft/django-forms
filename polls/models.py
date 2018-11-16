# Importamos los móculos que necesitamos
from django.db import models
from django.utils.timezone import now

# Definimos el modelo Reportes
class Reporter(models.Model):
    # Definimos los campos del modelo Reporter
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()

    # Implementamos el método __str__
    def __str__(self):
        return 'Autor: {}'.format(self.name)

# Definimos el modelo Question
class Question(models.Model):
    # Definimos el enumerativo para el campo 'target'
    TARGET_PEOPLE = (
        ('COMMON', 'Para todos'),
        ('STUDENTS', 'Alumnos'),
        ('TEACHER', 'Profesores'),
    )

    # Definimos los campos del modelo Question
    name = models.CharField('Nombre', max_length=10, blank=False, null=False, default='')
    pub_date = models.DateTimeField('Fecha de publicación', blank=True, null=True, default=now)
    target = models.CharField(
        # Indicamos la longitud máxima
        max_length=50,
        # Indicamos las opciones posibles que puede tomar este campo
        choices=TARGET_PEOPLE,
        # Indicamos la opción por defecto
        default=TARGET_PEOPLE[0][0],
        # Indicamos el texto helper a mostrar en un ModelForm
        help_text='Indique para que tipo de público esta destinada esta pregunta.'
    )
    reporter = models.ForeignKey(Reporter, blank=True, null=True, on_delete=models.CASCADE)

    # Definimos la clase Meta para el modelo Question
    class Meta:
        # Definimos el orden por defecto al recuperar el listado de preguntas
        ordering = ['id', '-pub_date']

    # Implementamos el método __str__
    def __str__(self):
        return 'Pregunta: {}'.format(self.name)

# Definimos el modelo Section
class Section(models.Model):
    # Definimos los campos del modelo Section
    name = models.CharField(max_length=255, blank=True, null=True)
    questions = models.ManyToManyField(Question)

    # Implementamos el método __str__
    def __str__(self):
        return 'Sección: {}'.format(self.name)