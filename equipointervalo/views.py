from django.shortcuts import render
from equipointervalo.models import Profesionales, Areas, Servicios
from equipointervalo.forms import FormularioAreas

# Create your views here.

def index (request):
    return render (request, "equipointervalo/index.html")

def profesionales (request):
    listado_profesionales = Profesionales.objects.all()
    return render (request, "equipointervalo/profesionales.html", {"profesionales": listado_profesionales})

def areas (request):
    listado_areas = Areas.objects.all()
    
    if request.GET.get ("nombre_area"):
        formulario = Areas(request.GET)
        if formulario.is_valid():
            data = formulario.cleaned_data
        listado_areas = Areas.objects.filter(nombre__icontains = request.GET.get ["nombre_area"]) 
        formulario = Areas()
        return render (request, "equipointervalo/areas.html", {"areas": listado_areas})

    else: 
        formulario = Areas()
        return render (request, "equipointervalo/areas.html", {"areas": listado_areas, "formulario": formulario})
    

def servicios (request):
    listado_servicios = Servicios.objects.all()
    return render (request, "equipointervalo/servicios.html", {"servicios": listado_servicios})



