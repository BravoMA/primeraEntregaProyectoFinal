from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import loader
from django.shortcuts import render
from familia.forms import PersonaForm, BuscarPersonasForm
from mascota.forms import MascotaForm, BuscarMascotasForm
from vehiculo.forms import VehiculoForm, BuscarVehiculosForm

from familia.models import Persona
from mascota.models import Mascota
from vehiculo.models import Vehiculo

def index(request):
    personas = Persona.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'personas': personas,
    }
    return HttpResponse(template.render(context, request))


def agregar(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue cargada con éxito
    '''

    if request.method == "POST":
        form = PersonaForm(request.POST)
        if form.is_valid():

            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            altura = form.cleaned_data['altura']
            Persona(nombre=nombre, apellido=apellido, email=email, fecha_nacimiento=fecha_nacimiento, altura=altura).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = PersonaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la persona fue eliminada con éxito        
    '''
    if request.method == "GET":
        persona = Persona.objects.filter(id=int(identificador)).first()
        if persona:
            persona.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar(request):
    if request.method == "GET":
        form_busqueda = BuscarPersonasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarPersonasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            personas = Persona.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"personas": personas})
    
def index2(request):
    mascotas = Mascota.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'mascotas': mascotas,
    }
    return HttpResponse(template.render(context, request))


def agregar2(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la mascota fue cargada con éxito
    '''

    if request.method == "POST":
        form = MascotaForm(request.POST)
        if form.is_valid():

            tipo = form.cleaned_data['tipo']
            nombre = form.cleaned_data['nombre']
            edad = form.cleaned_data['edad']
            
            Mascota(tipo=tipo, nombre=nombre, edad=edad).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = MascotaForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar2(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    la mascota fue eliminada con éxito        
    '''
    if request.method == "GET":
        mascota = Mascota.objects.filter(id=int(identificador)).first()
        if mascota:
            mascota.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar2(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar2(request):
    if request.method == "GET":
        form_busqueda = BuscarMascotasForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarMascotasForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            mascotas = Mascota.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"mascotas": mascotas})

def index3(request):
    vehiculos = Vehiculo.objects.all()
    template = loader.get_template('familia/lista_familiares.html')
    context = {
        'vehiculos': vehiculos,
    }
    return HttpResponse(template.render(context, request))


def agregar3(request):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    el vehiculo fue cargado con éxito
    '''

    if request.method == "POST":
        form = VehiculoForm(request.POST)
        if form.is_valid():

            tipo = form.cleaned_data['tipo']
            marca = form.cleaned_data['marca']
            modelo = form.cleaned_data['modelo']
            
            Vehiculo(tipo=tipo, marca=marca, modelo=modelo).save()

            return HttpResponseRedirect("/")
    elif request.method == "GET":
        form = VehiculoForm()
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")

    
    return render(request, 'familia/form_carga.html', {'form': form})


def borrar3(request, identificador):
    '''
    TODO: agregar un mensaje en el template index.html que avise al usuario que 
    el vehiculo fue eliminado con éxito        
    '''
    if request.method == "GET":
        vehiculo = Vehiculo.objects.filter(id=int(identificador)).first()
        if vehiculo:
            vehiculo.delete()
        return HttpResponseRedirect("/familia/")
    else:
        return HttpResponseBadRequest("Error no conzco ese metodo para esta request")


def actualizar3(request, identificador):
    '''
    TODO: implementar una vista para actualización
    '''
    pass


def buscar3(request):
    if request.method == "GET":
        form_busqueda = BuscarVehiculosForm()
        return render(request, 'familia/form_busqueda.html', {"form_busqueda": form_busqueda})

    elif request.method == "POST":
        form_busqueda = BuscarVehiculosForm(request.POST)
        if form_busqueda.is_valid():
            palabra_a_buscar = form_busqueda.cleaned_data['palabra_a_buscar']
            vehiculos = Vehiculo.objects.filter(nombre__icontains=palabra_a_buscar)

        return  render(request, 'familia/lista_familiares.html', {"mascotas": mascotas})
    