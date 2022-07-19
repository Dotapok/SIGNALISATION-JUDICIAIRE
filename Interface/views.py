from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'acceuil/index.html')

#inteface de l'utilisateur
def connexion(request):
    return render(request,'acceuil/interface.html')