from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#inteface de l'utilisateur
def Interface(request):
    return render(request,'acceuil/interface.html')