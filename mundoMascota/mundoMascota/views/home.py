from django.shortcuts import render
import requests


def home(request):
    
    api_url = "https://mindicador.cl/api"
    response = requests.get(api_url)
    print('status_code -> {0}'.format(response.status_code))
    json_request = response.json()
    print('json_request -> {0}'.format(json_request))
    dolar = json_request['dolar']['valor']
    fecha = json_request['dolar']['fecha']
    print('Retornar pagina home.html')
    return render(request, 'home.html', {'dolar': dolar, 'fecha': fecha})