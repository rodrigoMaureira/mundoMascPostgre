"""mundoMascota URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from mundoMascota.views.home import home
from mundoMascota.views.blog import Blog
from mundoMascota.views.login import login
from mundoMascota.views.principal import Principal
from mundoMascota.views.tienda import Tienda
from mundoMascota.views.contacto import contacto_index, formulario_contacto
from mundoMascota.views.mantenedorContacto import load_contacto
from mundoMascota.views.registro import registro_index, formulario_registro
#from mundoMascota.views.logout import logout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Principal),
    path('home',home),
    path('Tienda' ,Tienda),
    path('Blog',Blog),
    path('Contacto',contacto_index),
    path('contacto/formulario', formulario_contacto),
    path('mantenedorContacto',load_contacto),
    path('Registro', registro_index),
    path('registro/formulario', formulario_registro),
    path('login/', login),
    #path('logout/', logout)
]
