from django.shortcuts import render
from django.contrib.auth.models import User

def create_user(request):
    state = None
    message = None
    if request.method == 'POST':
        try:
            new_user = User()      
            #Leer datos de formulario y asignarlo al objeto que se persistira  	
            new_user.first_name = request.POST.get('first-name')
            new_user.last_name = request.POST.get('last-name')
            new_user.email = request.POST.get('email')
            new_user.set_password(request.POST.get('password'))
            #Persistir en la base de datos
            new_user.save()
            message = 'user updated.'
            state =True
        except Exception as e:
            print('Error: ', e)
            state = False
            message = 'error in create user.'            
    elif request.method == 'GET':
        print('GET') 
    return render(request, 'create-user.html', {'state': state, 'message': message})