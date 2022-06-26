from django.shortcuts import render
from mundoMascota.models import Contacto


def Principal(request):

    return render(request, "home.html")