from django.shortcuts import render
from mundoMascota.models import Contacto

def contacto_index(request):
    print('contacto_index')
    return render(request, 'contacto.html')

def formulario_contacto(request):
    print('formulario_contacto')

    if request.method == 'GET':
        print('invocación por método GET')
        nombre = request.GET.get('nombre')
        print('run {0}'.format(nombre))

    elif request.method == 'POST':
        print('invocación por método POST')
        #obtener información formulario
        #almacenandola en variables
        nombre = request.POST.get('nombre')
        apellidos = request.POST.get('apellidos')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        comentarios = request.POST.get('comentarios')
        #Crear un objecto Contacto
        #que posee relación con la tabla contacto
        contacto = Contacto()
        contacto.nombre = nombre
        contacto.apellidos = apellidos
        contacto.email = email
        contacto.telefono = telefono
        contacto.comentarios = comentarios
        contacto.save()
    return render(request, 'contacto.html')