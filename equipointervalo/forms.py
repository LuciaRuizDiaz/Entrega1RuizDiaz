from django.forms import Form,  CharField, IntegerField

class FormularioAreas(Form):
    nombre_area = CharField(max_length=150)
    