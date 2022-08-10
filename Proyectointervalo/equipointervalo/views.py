from django.shortcuts import render, HttpResponse
from equipointervalo.models import Profesionales, Areas, Servicios
from equipointervalo.forms import FormularioAreas, FormularioProfesionales

# Create your views here.

def index (request):
    
    listado_areas = Areas.objects.all()
    
    if request.GET.get ("nombre_area"):
        
        formulario = FormularioAreas(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_areas = Areas.objects.filter(nombre__icontains = data ["nombre_area"]) 

        return render (request, "equipointervalo/areas.html", {"areas": listado_areas})

    else: 
        formulario = FormularioAreas()
        return render (request, "equipointervalo/index.html", {"areas": listado_areas, "formulario": formulario})
    
    return render (request, "equipointervalo/index.html")

def profesionales (request):
    listado_profesionales = Profesionales.objects.all()
    return render (request, "equipointervalo/profesionales.html", {"profesionales": listado_profesionales})

def crear_profesional(request):

    if request.method == "GET":
        return render(request, "equipointervalo/profesionales.html")

    else:

        nombre = request.POST ["nombre"]
        apellido = request.POST["apellido"]  
        area = request.POST["area"]
        profesional = FormularioProfesionales (nombre=nombre, apellido=apellido, area=area)

        profesional.save()

    return render(request, "equipointervalo/profesionales.html")


def areas (request):
    
    listado_areas = Areas.objects.all()

    return render (request, "equipointervalo/index.html", {"areas": listado_areas})
    

def servicios (request):
    listado_servicios = Servicios.objects.all()
    return render (request, "equipointervalo/servicios.html", {"servicios": listado_servicios})



