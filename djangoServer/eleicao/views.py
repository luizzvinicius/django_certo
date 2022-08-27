from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'name': 'Biroliro'})


def add(request):

    num1 = int(request.GET['num1'])
    num2 = int(request.GET['num2'])
    res = num1 + num2

    return render(request, 'result.html', {'result': res})
