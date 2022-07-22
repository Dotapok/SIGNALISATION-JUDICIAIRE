from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'acceuil/index.html')

#inteface de l'utilisateur
def connexion(request):
    return render(request,'acceuil/interface.html')