from django.forms import Form,  CharField, IntegerField

class FormularioAreas(Form):
    nombre_area = CharField(max_length=150)
    
class FormularioProfesionales (Form):
    nombre= CharField(max_length=50)
    apellido= CharField(max_length=50)
    area = CharField(max_length=50)