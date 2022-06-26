from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(requeset):
    print('logout')

    try:
        logout(request)
    except Exception as e:
        