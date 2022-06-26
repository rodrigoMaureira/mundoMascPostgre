from django.shortcuts import render
from mundoMascota.models import Contacto

def Blog(request):

    return render(request, "Blog.html")