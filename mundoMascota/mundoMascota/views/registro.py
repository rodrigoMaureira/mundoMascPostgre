from django.shortcuts import render
from mundoMascota.models import Registro

def registro_index(request):
    print('registro_index')
    return render(request, 'registro.html')

def formulario_registro(request):
    print('formulario_registro')

    if request.method == 'GET':
        print('invocación por método GET')
        rut = request.GET.get('rut')
        print('run {0}'.format(rut))

    elif request.method == 'POST':
        print('invocación por método POST')
        #obtener información formulario
        #almacenandola en variables
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        rut = request.POST.get('rut')
        dv = request.POST.get ('dv')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        #Crear un objecto Registro
        #que posee relación con la tabla registro
        registro = Registro()
        registro.nombre = nombre
        registro.apellidos = apellidos
        registro.rut = rut
        registro.dv = dv
        registro.email = email
        registro.telefono = telefono
        registro.save()
    return render(request, 'registro.html')