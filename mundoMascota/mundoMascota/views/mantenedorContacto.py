from django.shortcuts import render
from mundoMascota.models import Contacto

def load_contacto(request):
    print('mantenedorContacto.py -> load_contacto')
    print('method -> ', request.method)
    if request.method == 'GET':
        try:
            codigo = request.GET['codigo']
            print('codigo ->', codigo)
            contacto = Contacto.objects.get(pk=codigo)
            contacto.delete()
        except Exception as i:
            print(i)
    if request.method == 'POST':
        try:
            id = request.POST['codigo']
            nombre= request.POST['nombre']
            apellidos = request.POST['apellidos']
            email = request.POST['email']
            telefono = request.POST['telefono']
            comentarios = request.POST['comentarios']
            contacto=Contacto.objects.get(pk=id)
            contacto.nombre = nombre
            contacto.apellidos = apellidos
            contacto.email = email
            contacto.telefono = telefono
            contacto.comentarios = comentarios
            contacto.save(force_update=True)
        except Exception as i:
            print(i)
    contactos = Contacto.objects.all
    return render(request, 'mantenedorContacto.html', {'contactos': contactos})