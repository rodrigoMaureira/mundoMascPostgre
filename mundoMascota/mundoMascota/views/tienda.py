from django.shortcuts import render
from mundoMascota.models import Contacto

def Tienda(request):

    return render(request, "Tienda.html")

def tienda_index(request):
    print('tienda_index')
    return render(request, 'tienda.html')

def formulario_tienda(request):
    print('formulario_tienda')

    if request.method == 'GET':
        print('invocación por método GET')
        run = request.GET.get('run')
        print('run {0}'.format(run))

    elif request.method == 'POST':
        print('invocación por método POST')
        #obtener información formulario
        #almacenandola en variables
        run = request.POST.get('run')
        dv = request.POST.get('dv')
        nombres = request.POST.get('nombres')
        apellido_paterno = request.POST.get('apellido-paterno')
        apellido_materno = request.POST.get('apellido-materno')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('asunto')
        #Crear un objecto Contacto
        #que posee relación con la tabla contacto
        tienda = Tienda()
        tienda.producto = run
        tienda.save()
    return render(request, 'tienda.html')