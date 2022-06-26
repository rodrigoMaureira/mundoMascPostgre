from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate

def load(request):
    try:
        print(request.method)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            login(request, user)
            user = authenticate (username=username, password=password)
            if user != None:
                print('Usuario Autenticado')
                redirect('home/')
            else:
                print('Error usuario o contraseña Invalida')
    except Exception as e:
        print 
    return render (request, 'login.html')