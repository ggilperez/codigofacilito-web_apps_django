from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html', {
        'message': 'Nuevo mensaje desde la vista',
        'title': 'Titulo'
    })
