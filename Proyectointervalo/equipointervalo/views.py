from django.shortcuts import render, HttpResponse
from equipointervalo.models import Profesionales, Areas, Servicios
from equipointervalo.forms import FormularioAreas, FormularioProfesionales, FormularioServicios

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

def formularioprofesionales (request):

    if request.method == "POST":
        miformulario= FormularioProfesionales (request.POST)
        
        print (miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            profesional = Profesionales (nombre=informacion['nombre'],apellido=informacion['apellido'],area=informacion['area'])
            profesional.save()
            return render(request, "equipointervalo/profesionales.html")

    else:

        miformulario = FormularioProfesionales()

    return render(request, "equipointervalo/formularioprofesionales.html", {"miformulario":miformulario})


def areas (request):
    
    listado_areas = Areas.objects.all()

    return render (request, "equipointervalo/index.html", {"areas": listado_areas})
    

def servicios (request):
    listado_servicios = Servicios.objects.all()
    return render (request, "equipointervalo/servicios.html", {"servicios": listado_servicios})



def formularioservicios (request):

    if request.method == "POST":
        miformulario= FormularioServicios (request.POST)
        
        print (miformulario)
        if miformulario.is_valid:
            informacion = miformulario.cleaned_data
            servicio = Servicios (nombre=informacion['nombre'], areaejecutora=informacion['areaejecutora'])
            servicio.save()
            return render(request, "equipointervalo/servicios.html")

    else:

        miformulario = FormularioServicios()

    return render(request, "equipointervalo/formularioservicios.html", {"miformulario":miformulario})