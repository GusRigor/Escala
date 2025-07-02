from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Essa é tela inicial para fazer escalas.")
