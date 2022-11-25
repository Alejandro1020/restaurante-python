# from urllib import request
from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioPlatos
from web.formularios.formularioEmpleados import FormularioEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.

#Todas las vistas son funciones de python 

def Home(request):
    return render(request, 'home.html' )

def PlatosVista(request):

    #rutina para consulat de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)

    #Esta vista va autilizar un formulario django debo crear entonces un objeto de la clase FormularioPlatos()
    formulario=FormularioPlatos

    #Creamos un diccionario para enviar el formulario al html(Template)
    data={
        'formulario':formulario,
        'bandera':False,
        'platos': platosConsultados
    }
    #Recibimos los datos del formulario
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #construir un diccionario de envio de datos hacia la BD

            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            #intentare llevar mis datos a la BD
            try:
                platoNuevo.save()
                data["bandera"]=True
                print("exito guardando")

            except Exception as error:
                print("upss", error)   
                data["bandera"]=False 
    return render(request,'menuplatos.html',data)

def EmpleadoVista(request): 

    formularioEmpleados= FormularioEmpleados

    datos={
        'formularioEmpleados':formularioEmpleados,
        'bandera':False
    }    
    if request.method=="POST":
        datosFormulario=FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #construir un diccionario de envio de datos hacia la BD

            empleadoNuevo=Empleados(
                nombre=datosLimpios["nombre"],                
                fotografia=datosLimpios["fotografia"],
                salario=datosLimpios["salario"],
                tipo=datosLimpios["tipo"],
                perfil=datosLimpios["perfil"]
            )
            #intentare llevar mis datos a la BD
            try:
                empleadoNuevo.save()
                print("exito guardando")
                datos["bandera"]=True

            except Exception as error:
                print("upss", error) 
                datos["bandera"]=False
    return render(request, 'empleados.html',datos)   

    #  id = models.IntegerField()
    # nombre = models.CharField(max_length=50)
    # fotografia = models.CharField(max_length=200)
    # salario = models.IntegerField()
    # tipo = models.IntegerField()
    # perfil = models.CharField(max_length=100)
