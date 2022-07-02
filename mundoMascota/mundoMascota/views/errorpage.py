from django.shortcuts import render

def error_401_page(request):
    return render(request, 'error-401.html')

def error_403_page(request):
    return render(request, 'error-403.html')